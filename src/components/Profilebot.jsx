import React from 'react'
import './Profilebot.css'
import { useState } from 'react';
const Profilebot =({ data, setEnablebot }) => {
    const [answer,setAnswer]=useState('');
    const [enableanswer,setEnableanswer]=useState(false);
    const [question,setQuestion]=useState('');
    const [form2,setForm2]=useState({});
    const [queue,setQueue]=useState([[]]);
    const setquery=(e)=>{
        e.preventDefault();
        setForm2({
            ...form2,
            [e.target.name]:e.target.value,
            ['player']:data
        })
    }
    const getanswer=(e)=>{
            e.preventDefault();
            fetch("http://localhost:8080/profileres", {
                method: 'POST',
                body: JSON.stringify(form2),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then((res) => {
                if (!res.ok) {
                    throw new Error('Network response was not ok');
                }
                // Check if the response content type is JSON
                const contentType = res.headers.get('content-type');
                if (!contentType || !contentType.includes('application/json')) {
                    throw new Error('Response was not JSON');
                }
                return res.json();
            })
            .then((data) => {
                setAnswer(data.answer);
                setQuestion(data.question);
                setEnableanswer(true);
                console.log(data.answer);
            })
            .catch((err) => {
                console.error('Error fetching data:', err);
                // Handle the error, such as displaying a message to the user
            });
        
        
    }
      return (
    <>
    <div className='main2'>
    <center>
    <div className='current-query'>
    {/* {queue.length>2 && <>Previously asked questions and answers by this user <br/>
    <table className='tble'>
    <tr><td>QUESTION</td><td>ANSWER</td></tr>
    {queue.map((dataItem,index) => (
                        <tr key={index}>
                            <td>{dataItem[0]}</td>
                            <td>{dataItem[1]}</td>
                        </tr>
                    ))}
                    </table></>} */}
                    <br /><br /><br />
    <button className='close' onClick={()=>{setEnablebot(false)}}>X</button><br />
    <label for='question'>ASK: </label>
    <input type='text' id='question' name='question' className='questionll' onChange={setquery}></input>
    <button className='btn' onClick={getanswer}> &#128269;</button>
    {enableanswer && <><div className='answer'>{answer}</div></>}
    </div>
    </center>
    </div>
    </>)
}

export default Profilebot