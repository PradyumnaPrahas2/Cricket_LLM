const express = require('express');
const server=express();
const cors = require('cors');
const bodyParser =require('body-parser');
const mongoose = require('mongoose');
const { stderr } = require('process');

main().catch(err=>console.log(err));

async function main(){
    await mongoose.connect('mongodb://localhost:27017/ODIWc');
    console.log('db connected')
}
const Tableschema = new mongoose.Schema({
    sno: Number,
    Team: String,
    matches: Number,
    won: Number,
    lost: Number ,
    pts:Number,
    NRR: Number
})
const queryschema= new mongoose.Schema({
    question:String,
    answer:String
})
const resultschema= new mongoose.Schema({
    match_no:Number,
    city:String,
    date_of_match:String,
    venue:String,
    Home_team:String,
    Away_team:String,
    toss_winner:String,
    winner:String,
    man_of_the_match:String,
    result:String,
    result_margin:Number,
    eliminator:String,
    umpire1:String,
    umpire2:String,
})
const Table = mongoose.model('2019',Tableschema);
const Table2=mongoose.model('2023',Tableschema);
const que=mongoose.model('questions',queryschema);
const results=mongoose.model('ipl_2023',resultschema);
server.use(cors());
server.use(bodyParser.json());
server.get('/results',(req,res)=>{
    results.find()
        .then(data=>res.json(data))
        .catch(err=>res.status(500).json(err))
})
server.post('/profileres',async(req,res)=>{
    console.log('this function has been called')
    let question = new que();
    // console.log("hi")
    console.log(req.body.question),
    question.player=req.body.player,
    question.question = req.body.question;
    const response_fun=()=>{
        console.log(doc)
        res.json(doc);
    }
    const {spawn}= require('child_process');
        // const childPython =spawn('python',['--version']);
    const childPython =spawn('python',[question.player+'.py',req.body.question]);
        childPython.stdout.on('data',(data)=>{
          const res=data.toString();
          question.answer=res;
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
    const doc= await question.save()
    console.log(doc)
})
server.get('/2019', (req, res) => {
    Table.find()
        .then(data => res.json(data))
        .catch(err => res.status(500).json(err));
});
server.get('/2023', (req, res) => {
    Table2.find()
        .then(data => res.json(data))
        .catch(err => res.status(500).json(err));
});
// server.get('/',async(req,res)=>{
//     console.log(req.body)
//     // console.log("kkkkkk")
//     let user= await Login.findOne(req.body)
//     console.log(user);
//     if(user){
//         res.status(200).send(true)
//     }
//     else{
//         res.status(500).send(false)
//     }
// })

server.post('/query',async(req,res)=>{
    let question = new que();
    // console.log("hi")
    console.log(req.body.question),
    question.question = req.body.question;
    const response_fun=()=>{
        console.log(doc)
        res.json(doc);
    }
    const {spawn}= require('child_process');
        // const childPython =spawn('python',['--version']);
    const childPython =spawn('python',['chatbot.py',req.body.question]);
        childPython.stdout.on('data',(data)=>{
          const res=data.toString('utf8');
          question.answer=res;
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
    const doc= await question.save()
    console.log(doc)
})
server.listen(8080,()=>{
    console.log('server started')
})