import React, { useState } from 'react'
import axios from 'axios';
import Profilebot from './Profilebot';
import  { useEffect } from 'react';
import ReactPlayer from 'react-player';
import Chart from 'react-apexcharts';
const playedid={
  '':'',
  'Virat Kohli':'virat',
  'Sachin Tendulkar':'sachin',
  'Ab devilliers':'abd',
  'Shane warne':'warne',
  'MS Dhoni':'dhoni'
}
const videolinks={
  'virat':['video1','video2','video3','video4','video5'],
  'sachin':['video1','video2','video3','video4','video5'],
  'abd':['video1','video2','video3','video4','video5'],
  'warne':['video1','video2','video3','video4','video5'],
  'dhoni':['video1','video2','video3','video4','video5']
}
const images={
  'virat':'https://th.bing.com/th/id/OIP.wyuSPln14Y8FyyJo9VDSQQAAAA?w=165&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7',
  'dhoni':'data:image/jpeg;base64,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',
  'warne':'https://th.bing.com/th/id/OIP.dcCGfeRDE8aNVI1bva1z_QHaGs?w=188&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7',
  'sachin':'https://th.bing.com/th/id/OIP.zKC9l155Tc8s5K_MeL5CxAAAAA?w=219&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7'
  ,'abd':'data:image/jpeg;base64,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'}
const player_profile={'':'','sachin':'https://www.espncricinfo.com/cricketers/sachin-tendulkar-35320/bowling-batting-stats',
'virat':"https://www.espncricinfo.com/cricketers/virat-kohli-253802/bowling-batting-stats",
'dhoni':'https://www.espncricinfo.com/cricketers/ms-dhoni-28081/bowling-batting-stats',
'warne':'https://www.espncricinfo.com/cricketers/shane-warne-8166/bowling-batting-stats',
'abd':'https://www.espncricinfo.com/cricketers/ab-de-villiers-44936/bowling-batting-stats'}
const Profiles = () => {
  const videoUrl = 'https://youtu.be/IJNg23jMFjc?feature=shared'
    const [playerdata,setPlayerdata]=useState([]);
    const[videos,setVideos]=useState(false);
    const[currset,setCurrset]=useState(false);
    const [current,setCurrent]=useState('');
    const[enablebot,setEnablebot]=useState(false);
    const[enablestat,setEnablestat]=useState(false);
    const[visual,setVisual]=useState(false);
    const[closevideo,setclosevideo]=useState(false);
    const[selectedvideo,setselectedvideo]=useState('');
    const[filteredarr,setfilteredarr]=useState([])
    const[selectedurl,setselectedurl]=useState('');
    const[selectdetitle,setselectedtitle]=useState('');
    const[playername,setplayername]=useState('');
    const[matches,setMatches]=useState([])
    const availableplayers=['Virat Kohli','Sachin Tendulkar','Ab devilliers','MS Dhoni','Shane Warne']
    const handleChange = (event) => {
      const selectedIndex = event.target.value;
      setselectedurl(filteredarr[selectedIndex][1]);
      setselectedtitle(filteredarr[selectedIndex][0]);
      setclosevideo(true);
    };
    const selectplayers=(e)=>{
      e.preventDefault();
      setplayername(e.target.value);
    }
    const searchplayers=(e)=>{
      function findMatchingPlayers(input) {
        const lowerInput = input.toLowerCase();
        return availableplayers.filter(player => player.toLowerCase().includes(lowerInput));
        }
        const userInput = playername; 
        const matchingPlayers = findMatchingPlayers(userInput);
        
        if (matchingPlayers.length > 0) {
            console.log(`Matching players: ${matchingPlayers.join(', ')}`);
        } else {
            console.log(`No matching players found for "${userInput}".`);
        }
        setMatches(matchingPlayers);
    }
    const Dropdown = ({ filteredarr }) => {
      // Check if the array size is greater than 0
      if (!Array.isArray(filteredarr)) {
        const data = filteredarr;
          const cleanedData = data.trim();
          const trimmedData = cleanedData.slice(1, -1);
          const items = trimmedData.split('],');
          const result = [];
          for (let i = 0; i < items.length; i++) {
              let item = items[i].trim();
              // Remove any leading or trailing square brackets
              item = item.replace(/\[|\]/g, '');
              // Split the item into description and URL based on the comma ','
              const parts = item.split(',');
              // Trim each part and remove any single quotes
              const cleanedParts = parts.map(part => part.trim().replace(/'/g, ''));
              // Push the cleaned parts to the result array as a 2D inner array
              result.push(cleanedParts);
          }

          console.log(typeof result);
          if (Array.isArray(result)) {
            console.log('result is an array');
            setfilteredarr(result);
        } else {
            console.log('result is not an array');
        }

    }
      try{
      if (filteredarr.length === 0) {
        return <p>No data available</p>;
      }
    else{
      return (
        <div>
          <select onChange={handleChange}>
          {filteredarr.map((item, index) => (
          <option key={index} value={index}>
            {item[0]}
          </option>
        ))}
          </select>
          {selectedurl && <><p>Selected video title:{selectdetitle}</p><p>Selected video url: {selectedurl}</p></>}
        </div>
      );
    }}
    catch(error){
      console.log("exception handled"+error);
    }
  };
    const changevideovalue=(e)=>{
      e.preventDefault();
      setselectedvideo(e.target.value);
    }
    const videollm=async(e)=>{
      e.preventDefault();
      try {
        const url = selectedvideo;
        console.log(url);
        const response = await axios.post("http://localhost:8082/video", { url });
        console.log(response.data);
        setfilteredarr(response.data);
      } catch (error) {
        console.error('Error in llm');
      }
        };
    const bot=(e)=>{
      e.preventDefault();
      setEnablebot(true);
    }
    const set=(e)=>{
      e.preventDefault();
      setCurrent(e.target.value);
      setCurrset(true);
    }
    const visualize = async () => {
      setVisual(true);
      setEnablestat(false);
      setVideos(false);
    }
    const video=(e)=>{
      e.preventDefault();
      setVisual(false);
      setEnablestat(false);
      setVideos(true);
    }
    const VideoPlayer = ({ url }) => {
      return (
        <div className="video-player">
          <ReactPlayer url={url} controls={true} width="100%" height="100%" />
        </div>
      );
    };
    const execute=async(e)=>{
      e.preventDefault();
      setVisual(false);
      setEnablestat(true);
        // const currentValue = e.target.value;
        try {
          // setCurrent(currentValue);
          setCurrset(true);
          const url = player_profile[current];
          console.log(url);
          const response = await axios.post("http://localhost:8082/player", { url });
          setPlayerdata(response.data.tableData);
        } catch (error) {
          console.error('Error scraping table:', error);
        }
          };
      
  return (
    <>
    <div className='playerprofile'>
      <div className='sc'>
    <input type='text' placeholder='Enter player to search for' id='nameoftheplayer' onChange={selectplayers}></input>
    <button onClick={searchplayers} className='search'>&#128269;</button>
    </div>
    {matches.length!=0 ?(<>
    <br/>
      {matches.map((player, index) => (
        <div className='co'>
        <div className={index} style={{ display: 'flex', alignItems: 'center', marginBottom: '10px' }}>
        <img src={images[playedid[player]]} style={{ width: '50px', height: '50px' }}></img>
        <button className='inner-btn' onClick={set} style={{ width: '500px', height: '50px', marginLeft: '5px' }} value={playedid[player]}>{playedid[player]}
        </button>
        </div>
        </div>
      ))}
    </>):(<><p>No results found</p></>)}
    {/* <button onClick={set} value='sachin'>sachin</button>
    <button onClick={set} value='virat'>virat</button>
    <button onClick={set} value='dhoni'>dhoni</button>
    <button onClick={set} value='warne'>warne</button>
    <button onClick={set} value='abd'>abd</button><br/> */}
    <div className='options'>
      <div className='flex-container'>
      {currset && <><img className='profileimg' src={images[current]}></img></>}
    <button onClick={bot} className='BERT'>talk to bot</button>
    <br/>
    </div>
    </div>
    <button onClick={execute} className='stat'>SHOW STATISTICS</button>
    <button onClick={visualize} className='picstat'>VISUALIZE STATISTICS</button>
    <button onClick={video} className='vdo'>VIDEO LINKS</button>
    <a href=''>NEWS</a>
    {(visual && current!='') &&<>
    <React.Fragment>
    {current=='virat' &&
      <div className='bar'>
        <Chart
        type="bar"
        width={600}
        height={300}
        series={[
          {
          name:'No.of runs of '+{current},
          data:[280,600,210,388,765,432]
        }
      ]}
        options={{
          title:{text:"Virat Kohli's runs distribution"},
          style:{ fontSize:20},
          xaxis:{
            categories:['Delhi','Mumbai','Chennai','Hyderabad','Bangalore','Mohali'],
            title:{text:"venue"}
          }
        }}
        ></Chart>
      </div>}
      {current=='dhoni' &&
      <div className='bar'>
        <Chart
        type="bar"
        width={600}
        height={300}
        series={[
          {
          name:'No.of runs of '+{current},
          data:[80,390,908,310,665,279]
        }
      ]}
        options={{
          title:{text:"Dhoni's runs distribution"},
          style:{ fontSize:20},
          xaxis:{
            categories:['Ahmedabad','Mumbai','Chennai','Hyderabad','Bangalore','Mohali'],
            title:{text:"venue"}
          }
        }}
        ></Chart>
      </div>}
      {current=='sachin' &&
      <div className='bar'>
        <Chart
        type="bar"
        width={600}
        height={300}
        series={[
          {
          name:'No.of runs of '+{current},
          data:[280,600,210,388,765,432]
        }
      ]}
        options={{
          title:{text:"Sachins's runs distribution"},
          style:{ fontSize:20},
          xaxis:{
            categories:['Kolkata','Mumbai','Chennai','Hyderabad','Bangalore','Delhi'],
            title:{text:"venue"}
          }
        }}
        ></Chart>
      </div>}
      {current=='abd' &&
      <div className='bar'>
        <Chart
        type="bar"
        width={600}
        height={300}
        series={[
          {
          name:'No.of runs of '+{current},
          data:[7799,2671,6710,1688,1565,1832]
        }
      ]}
        options={{
          title:{text:"Ab devilliers's runs distribution"},
          style:{ fontSize:20},
          xaxis:{
            categories:['South Africa','Australia','India','England','NewZealand','Pakistan'],
            title:{text:"venue"}
          }
        }}
        ></Chart>
      </div>}
      {current=='warne' &&
      <div className='bar'>
        <Chart
        type="bar"
        width={600}
        height={300}
        series={[
          {
          name:'No.of wickets of '+{current},
          data:[491,266,129,190,203,100,99]
        }
      ]}
        options={{
          title:{text:"Shane warne's wickets distribution"},
          style:{ fontSize:20},
          xaxis:{
            categories:['Australia','England','India','South Africa','West Indies','Pakistan','New Zealand','Sri Lanka'],
            title:{text:"venue"}
          }
        }}
        ></Chart>
      </div>}
      </React.Fragment>

    </>}
    {enablebot && <Profilebot data={current} setEnablebot={setEnablebot}/> }
    {(enablestat && current!='') &&<>
    <h2>Statistics of {current} </h2>
            <table>
        <tbody>
          {playerdata.map((row, rowIndex) => {
              return (
                <tr key={rowIndex}>
                  {row.map((cell, cellIndex) => (
                    <td key={cellIndex}>{cell}</td>
                  ))}
                </tr>
              );
          })}
        </tbody>
      </table>
      </>}
      {videos && <><div className="App">
        <input type="text" placeholder='Search' onChange={changevideovalue}/><button onClick={videollm}>&#128269;</button>
        <div className="App">
          <Dropdown filteredarr={filteredarr} />
        </div>
        {closevideo &&<><h1>Video Player</h1>
          <button onClick={(e)=>{setclosevideo(false)}}>X</button>
          <VideoPlayer url={selectedurl} /></>}
    </div>
      </>}
      </div>
    </>
        
  )
}

export default Profiles