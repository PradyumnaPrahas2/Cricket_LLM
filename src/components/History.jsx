import React from 'react'
import './Predict.css'
const History = () => {
  return (
    <>
    <div className='history'>
    <table className='ResultTable'>
        <tr>
        <th>Match No.</th>
        <th>TEAM 1</th>
        <th>TEAM 2</th>
        <th>TOSS WINNER</th>
        <th>TOSS DECISION</th>
        <th> ACTUAL WINNER</th>
        <th> PREDICTED WINNER</th>
        </tr>
        <tr>
            <th>1</th>
        <th>Chennai Super Kings</th>
        <th>Royal Challengers Bengaluru</th>
        <th>RCB</th>
        <th>BAT</th>
        <th> CSK</th>
        <th className='rowcorrect-ans'> CSK</th>
        </tr>
        <tr>
            <th>2</th>
        <th>Punjab Kings</th>
        <th>Delhi Capitals</th>
        <th>PBKS</th>
        <th>FIELD</th>
        <th> PBKS</th>
        <th className='rowcorrect-ans'> PBKS</th>
        </tr>
        <tr>
            <th>3</th>
        <th>Kolkata Knight Riders</th>
        <th>Sunrisers Hyderabad</th>
        <th>SRH</th>
        <th>FIELD</th>
        <th> KKR</th>
        <th className='rowcorrect-ans'> KKR</th>
        </tr>
        <tr>
            <th>4</th>
        <th>Rajasthan Royals</th>
        <th>Lucknow Super Giants</th>
        <th>LSG</th>
        <th>FIELD</th>
        <th>RR</th>
        <th className='rowcorrect-ans'>RR</th>
        </tr>
        <tr>
            <th>5</th>
        <th>Gujarat Titans</th>
        <th>Mumbai Indians</th>
        <th>MI</th>
        <th>FIELD</th>
        <th>GT</th>
        <th className='rowincorrect-ans'>MI</th>
        </tr>
        <tr>
            <th>6</th>
        <th>Royal Challengers Bengaluru</th>
        <th>Punjab Kings</th>
        <th>RCB</th>
        <th>FIELD</th>
        <th>RCB</th>
        <th className='rowcorrect-ans'>RCB</th>
        </tr>
    </table>
    <center>
        Last 5 predictions<br/>
    <span className="tick">&#10003;</span> <span className="cross">&#10005;</span><span className="tick">&#10003;</span><span className="tick">&#10003;</span><span className="tick">&#10003;</span>
    <br/>
    <a href='/Points'>Check out points table</a>
    </center>
    <center>By | Pradyumna Prahas|KMIT</center>
    </div>
    </>
  )
}

export default History