import React, { useState } from 'react'
import './Llm.css'
const Llm = () => {
    const [answer,setAnswer]=useState('');
    const [enableanswer,setEnableanswer]=useState(false);
    const [question,setQuestion]=useState('');
    const [form,setForm]=useState({});
    const [queue,setQueue]=useState([[]]);
    const setquery=(e)=>{
        e.preventDefault();
        setForm({
            ...form,
            [e.target.name]:e.target.value})
    }
    const getanswer=(e)=>{
        e.preventDefault();
        fetch("http://localhost:8080/query",{
        method:'POST',body:JSON.stringify(form),
        headers:{
            'Content-Type':'application/json'
        }
        })
        .then((res)=>res.json())
        .then((data)=>{setAnswer(data.answer)
          setQuestion(data.question)
        setEnableanswer(true)
        console.log(data.answer)
        })
        .catch((err)=>console.log(err))
        // setQueue(prev=>[...prev,[question,answer]]);
        setQueue(prev=>{
          const newQueue = [...prev, [question, answer]];
          if (newQueue.length > 7) {
              // If the length exceeds 7, remove the first element
              newQueue.shift();
          }
          return newQueue;
        })
        // queue.forEach((element, index) => {
        //     console.log(`Index ${index}: ${element}`);
        //   });
        }
      return (
    <>
    <div className='main'>
    <center>
    <div className='current-query'>
    {queue.length>2 && <>Previously asked questions and answers by this user <br/>
    <table className='tble'>
    <tr><td>QUESTION</td><td>ANSWER</td></tr>
    {queue.map((dataItem,index) => (
                        <tr key={index}>
                            <td>{dataItem[0]}</td>
                            <td>{dataItem[1]}</td>
                        </tr>
                    ))}
                    </table></>}
    <label for='question'>ASK: </label>
    <input type='text' id='question' name='question' className='questionl' onChange={setquery}></input>
    <button className='btn' onClick={getanswer}> &#128269;</button>
    {enableanswer && <><div className='answer'>{answer}</div></>}
    </div>
    </center>
    </div>
    </>
  )
}

export default Llm