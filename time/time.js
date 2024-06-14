const express = require('express');
const server=express();
const cors = require('cors');
const bodyParser =require('body-parser');
main().catch(err=>console.log(err));

server.use(cors());
server.use(bodyParser.json());


server.post('/time',async(req,res)=>{
    console.log(req.body)
    const {spawn}= require('child_process');
        // const childPython =spawn('python',['--version']);
        const childPython =spawn('python',['timeandweather.py',req.body.country,req.body.city]);
        childPython.stdout.on('data',(data)=>{
          console.log(data);
        });
        childPython.stderr.on('data',(data)=>{
          console.log('Error sending info to python file');
        });
        childPython.on('close',(code)=>{
          console.log((code))
        })
    res.json(req.body);
})

server.listen(8086,()=>{
    console.log('server started')
})