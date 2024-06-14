const express = require('express');
const server=express();
const cors = require('cors');
const axios=require('axios')
const bodyParser =require('body-parser');
const mongoose = require('mongoose');
const { stderr } = require('process');

main().catch(err=>console.log(err));

async function main(){
    await mongoose.connect('mongodb://localhost:27017/ipl');
    console.log('db connected')
}
const loginSchema = new mongoose.Schema({
    TossWinner: String,
    TossDecision: String,
    Team1: String,
    Team2: String,
    Venue: String ,
    Result:String,
})
const queryschema= new mongoose.Schema({
  question:String,
  answer:[String]
})
const que=mongoose.model('questions',queryschema);
const Login = mongoose.model('Ipldata',loginSchema);
server.use(cors());
server.use(bodyParser.json());
server.get('/ipldatas', (req, res) => {
    Login.find()
        .then(data => res.json(data))
        .catch(err => res.status(500).json(err));
});
server.get('/',async(req,res)=>{
    console.log(req.body)
    // console.log("kkkkkk")
    let user= await Login.findOne(req.body)
    console.log(user);
    if(user){
        res.status(200).send(true)
    }
    else{
        res.status(500).send(false)
    }
})

server.post('/demo',async(req,res)=>{
    let login = new Login();
    // console.log("hi")
    console.log(req.body)
    login.Team1 = req.body.Team1;
    login.Team2 = req.body.Team2;
    login.Venue = req.body.Venue;
    login.TossWinner = req.body.TossWinner;
    login.TossDecision=req.body.TossDecision;
    const response_fun=()=>{
        console.log(doc)
        res.json(doc);
    }
    const {spawn}= require('child_process');
        // const childPython =spawn('python',['--version']);
    const childPython =spawn('python',['iplmodel.py',req.body.Team1,req.body.Team2,req.body.Venue,req.body.TossWinner,req.body.TossDecision]);
        childPython.stdout.on('data',(data)=>{
          const res=data.toString();
          login.Result=res;
        //   const doc= await login.save()
          console.log(res);
        });
        childPython.stderr.on('data',(data)=>{
          console.log(data);
        });
        childPython.on('close',(code)=>{
          console.log((code))
          response_fun();
        })
    const doc= await login.save()
    // console.log(doc)
})
const cheerio = require('cheerio');

// Assuming 'htmlString' contains the raw HTML of the webpage
server.post('/player', (req, res) => {
  console.log(req.body);
  const { url } = req.body;

  axios.get(url)
    .then(response => {
      const html = response.data;

      const $ = cheerio.load(html);

      const table = $('table');

      const headings = [];
      table.find('th').each((i, th) => {
        headings.push($(th).text().trim());
      });

      const tableData = [];
      table.find('tr').each((i, row) => {
        const rowData = [];
        $(row).find('td, th').each((j, cell) => {
          rowData.push($(cell).text().trim());
        });
        tableData.push(rowData);
      });

      res.json({ headings, tableData });
    })
    .catch(error => {
      console.error('Error scraping table:', error);
      res.status(500).json({ error: 'Internal server error' });
    });
});
server.post('/video',(req,res)=>{
  const context=req.body.url;
  console.log(context)
  let responseList=[]
  const response_fun=()=>{
        console.log(responseList)
        res.json(responseList);
    }
  const {spawn}= require('child_process');
  const childPython =spawn('python',['videollm.py',context]);
        childPython.stdout.on('data',(data)=>{
          console.log('Received data from stdout:', data.toString().trim());
        try {
          const receivedData = data.toString().trim(); // Parse the data as JSON (if needed)
        responseList = receivedData; 
        } catch (error) {
            // If parsing fails, log the error
            console.error('Error parsing JSON:', error);
        }
        });
        childPython.stderr.on('data',(data)=>{
          const data2 = [['Option 1', 'Other data 1'], ['Option 2', 'Other data 2']];
          console.log(data);
          const res=JSON.parse(JSON.stringify(data2));
          responseList = res; 
          // console.log(res);
        });
        childPython.on('close',(code)=>{
          console.log((code))
          response_fun();
        })
    // console.log(responseList);
})
server.post('/year', (req, res) => {
    console.log(req.body)
  const {url}=req.body;
    // Fetch webpage content
    axios.get(url)
      .then(response => {
        const html = response.data;
  
        // Load HTML content into Cheerio
        const $ = cheerio.load(html);
  
        // Find the table element
        const table = $('table').first();
  
        // Extract data from the table
        const tableData = [];
        table.find('tr').each((i, row) => {
          const rowData = [];
          $(row).find('td, th').each((j, cell) => {
            rowData.push($(cell).text().trim());
          });
          tableData.push(rowData);
        });
  
        // Send the extracted table data to the client
        res.json({ tableData });
      })
      .catch(error => {
        console.error('Error scraping table:', error);
        res.status(500).json({ error: 'Internal server error' });
      });
  });
server.listen(8082,()=>{
    console.log('server started')
})