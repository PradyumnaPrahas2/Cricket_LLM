import React from 'react'
import { useEffect, useState } from "react";
import './Predict.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlane } from '@fortawesome/free-solid-svg-icons';
import e from 'cors';
const countries = [
    {name:"NULL",value:"NULL",cities:["null"]},
  { name: "SRH", value: "SRH", cities: ["NULL","RCB", "CSK",'MI','RR','LSG','KKR','GT','DC','PBKS'] },
  { name: "RCB", value: "RCB", cities: ["NULL","SRH", "CSK",'MI','RR','PBKS','KKR','LSG','GT','DC'] },
  { name: "RR", value: "RR", cities: ["NULL","SRH", "CSK",'MI','RCB','PBKS','KKR','LSG','GT','DC'] },
  { name: "PBKS", value: "PBKS", cities: ["NULL","SRH", "CSK",'MI','RR','RCB','KKR','LSG','GT','DC'] },
  { name: "CSK", value: "CSK", cities: ["NULL","SRH", "RCB",'MI','RR','PBKS','KKR','LSG','GT','DC'] },
  { name: "MI", value: "MI", cities: ["NULL","SRH", "CSK",'RCB','RR','PBKS','KKR','LSG','GT','DC'] },
  { name: "LSG", value: "LSG", cities: ["NULL","SRH", "CSK",'MI','RR','PBKS','KKR','RCB','GT','DC'] },
  { name: "GT", value: "GT", cities: ["NULL","SRH", "CSK",'MI','RR','PBKS','KKR','LSG','RCB','DC'] },
  { name: "KKR", value: "KKR", cities: ["NULL","SRH", "CSK",'MI','RR','PBKS','RCB','LSG','GT','DC'] },
  { name: "DC", value: "DC", cities: ["NULL","SRH", "CSK",'MI','RR','PBKS','KKR','LSG','GT','RCB'] },
];
const teams = [
  {name:"NULL",value:"NULL",cities:["null"]},
{ name: "SRH", value: "SRH", cities: ["Bhuvneshwar Kumar","Abdul Samad", "Washington Sundar",'Abhishek Sharma','Mayank Agarwal','Rahul Tripathi','Shahbaz Ahmed','Mayank Markande','T Natarajan','Nitish Reddy','Jaydev Unadkat','Umran Malik','J Subhramanyan','Sanvir Singh'] },
{ name: "RCB", value: "RCB", cities: ["Rajat Patidar","Suyash P", "Virat Kohli",'M Lomror','M Siraj','Mayank Dagar','Swapnil Singh','Dinesh Karthik','Anuj Rawat','Karn Sharma','Yash Dayal','Akash Deep','V Vyshak'] },
{ name: "RR", value: "RR", cities: ['Jaiswal','K S Rathore','S Dubey','R parag','R Ashwin','Dhruv Jurel','S. Samson','Avesh khan','Sandeep Sharma','Navdeep Saini','Chahal','Kuldeep sen','Tanush'] },
{ name: "PBKS", value: "PBKS", cities: ['Shikar Dhawan','Harpreet','S Singh','A Taide','V Sing','A Sharma','R Dhawan','T Tyagarajan','Prabhsimran','Jitesh','R Chahar','Harshal','Arshdeep','Price Choudhary'] },
{ name: "CSK", value: "CSK", cities: ['Gaikwad','Rahane','Rasheed','Rizvi','Nishant sindhu','S Dube','Jadeja','Dhoni','Avanish','AJ Mandal','Hangargekar','D Chahar','M Choudhary','S Thakur','T Deshpande'] },
{ name: "MI", value: "MI", cities: ['Rohit Sharma','Nehal wadhera','S Yadav','Tilak Varma','Naman','Shivalik','Hardik','Shams Mulani','Karthikeya','A Tendulkar','Kishan','Chawla','Bumrah','Madhwal'] },
{ name: "LSG", value: "LSG", cities: ['Mankad','Padikkal','Krunal','Hooda','Kulkarni','Badoni','Gowtham','Mavi','KL Rahul','Bishnoi','Mayank Yadav','Yash','Amit Mishra','Mohsin','Arshad Khan'] },
{ name: "GT", value: "GT", cities: ['Gill','Sudharshan','Abhinav Manohar','Shahrukh','Tewatia','Shankar','Saha','Tyagi','Sai Kishore','Mohit','Nalkande','Jayant','Umesh','Sandeep warrier'] },
{ name: "KKR", value: "KKR", cities: ['Manish Pandey','Ramandeep','Rinku','Shreyas','Nitish Rana','Sakib','V Iyer','Anukul','Bharat','Vaibhav','Suyash','Chakravarthy','Sakariya','Harshit Rana'] },
{ name: "DC", value: "DC", cities: ['Bhui','Yash Dhull','Shaw','Lalit','Axar','Sumit','Abhishek','Pant','Ishant','Rasikh','Khaleel','Ostwal','Kuldeep','P Dubey'] },
];
const overseasteams = [
  {name:"NULL",value:"NULL",cities:["null"]},
{ name: "SRH", value: "SRH", cities: ['Travis Head','Pat Cummins','F Farooqi','Marco Jansen','Heinrich Klaasen','Aiden Markram','Glenn Phillips'] },
{ name: "RCB", value: "RCB", cities: ["Faf du Plesis","Glenn Maxwell", "Tom Curran",'Alzarri Joseph','Lockie Ferguson','Reece Topley','C GREEN'] },
{ name: "RR", value: "RR", cities: ['Hetmyer','Buttler','Boult','Nandre Burger','Tom Kohler-Cadmore','D Ferreira'] },
{ name: "PBKS", value: "PBKS", cities: ['Rilee Rossouw','LivingStone','S Raza','Chris Woakes','Bairstow','Ellis','Rabada'] },
{ name: "CSK", value: "CSK", cities: ['Moeen Ali','Mitchell','M Santner','Ravindra','Mustafizur','M Theekshana'] },
{ name: "MI", value: "MI", cities: ['Tim David','Brevis','Nabi','R Shepherd','Coetzee','Thushara','L Wood','K Maphaka'] },
{ name: "LSG", value: "LSG", cities: ['K Mayers','Stoinis','Turner','Willey','Pooran','de Kock','Naveen Ul-Haq','Shamar Joseph'] },
{ name: "GT", value: "GT", cities: ['Miller','Williamson','Omarzai','Rashid','Wade','Noor','Little','Spencer'] },
{ name: "KKR", value: "KKR", cities: ['Rutherford','Narine','Russell','Gurbaz','Salt','Starc','Chameera','Mujeeb'] },
{ name: "DC", value: "DC", cities: ['Warner','Marsh','J Fraser Mc-Gurk','Marsh','Stubbs','J Richardson','Nortje'] },
];
const venue=[{name:'NULL',value:0},{name:'Ahmedabad',value:0},
{name:'Kolkata',value: 1},
{name:'Mumbai',value: 2},
{name:'Navi Mumbai',value: 3},
{name:'Pune',value: 4},
{name:'Dubai',value: 5},
{name:'Sharjah',value: 6},
{name:'Abu Dhabi',value: 7},
{name:'Delhi',value: 8},
{name:'Chennai',value: 9},
{name:'Hyderabad',value: 10},
{name:'Visakhapatnam',value: 11},
{name:'Chandigarh',value: 12},
{name:'Bengaluru',value: 13},
{name:'Jaipur',value: 14},
{name:'Indore',value: 15},
{name:'Kanpur',value: 16},
{name:'Rajkot',value: 17},
{name:'Raipur',value: 18},
{name:'Ranchi',value: 19},
{name:'Cuttack',value: 20},
{name:'Dharamsala',value: 21},
{name:'Kochi',value: 22},
{name:'Nagpur',value: 23},
{name:'Johannesburg',value: 24},
{name:'Centurion',value: 25},
{name:'Durban',value: 26},
{name:'Bloemfontein',value: 27},
{name:'Port Elizabeth',value: 28},
{name:'Kimberley',value: 29},
{name:'East London',value: 30},
{name:'Cape Town',value: 31}]
const dictionary2={"SRH\r\n":"https://th.bing.com/th?id=OIP.cMarPH0NiYx4KXdB8xI9hgHaFj&w=288&h=216&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2","CSK\r\n":"https://th.bing.com/th/id/OIP.dXUJQG4cK2U87IgjNrUpAwHaGl?w=181&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7","RCB\r\n":"https://th.bing.com/th?id=OIF.PB8YoYjx13GkTCwc1GwBHw&w=294&h=212&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2","RR\r\n":"https://th.bing.com/th/id/OIP.0F7IybavryIVpYMz0C4LFgHaEK?w=286&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7","MI\r\n":"https://th.bing.com/th/id/OIP.I4J2tbscJwV5UC5OwNxzmgHaEZ?w=298&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7","LSG\r\n":"https://th.bing.com/th/id/OIP.4avNOAmjN7ztchghLUTLMwHaEK?w=319&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7","PBKS\r\n":"https://th.bing.com/th/id/OIP.eCYw-5MAfetpxfLYY_eA5wHaEC?w=242&h=181&c=7&r=0&o=5&dpr=1.3&pid=1.7","DC\r\n":"https://th.bing.com/th/id/OIP._RKRMyHQIpRpJ80OVVsRQwAAAA?w=289&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7","KKR\r\n":"https://th.bing.com/th/id/OIP.0Qy5xuN_RR77ChrUv_C_sQHaFj?w=239&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7","GT\r\n":"https://th.bing.com/th/id/OIP.DXNDJzjBE_PWMH1OG38uvgHaFS?w=253&h=181&c=7&r=0&o=5&dpr=1.3&pid=1.7"}
const dictionary={"SRH":"https://th.bing.com/th?id=OIP.cMarPH0NiYx4KXdB8xI9hgHaFj&w=288&h=216&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2","CSK":"https://th.bing.com/th/id/OIP.dXUJQG4cK2U87IgjNrUpAwHaGl?w=181&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7","RCB":"https://th.bing.com/th?id=OIF.PB8YoYjx13GkTCwc1GwBHw&w=294&h=212&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2","RR":"https://th.bing.com/th/id/OIP.0F7IybavryIVpYMz0C4LFgHaEK?w=286&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7","MI":"https://th.bing.com/th/id/OIP.I4J2tbscJwV5UC5OwNxzmgHaEZ?w=298&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7","LSG":"https://th.bing.com/th/id/OIP.4avNOAmjN7ztchghLUTLMwHaEK?w=319&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7","PBKS":"https://th.bing.com/th/id/OIP.eCYw-5MAfetpxfLYY_eA5wHaEC?w=242&h=181&c=7&r=0&o=5&dpr=1.3&pid=1.7","DC":"https://th.bing.com/th/id/OIP._RKRMyHQIpRpJ80OVVsRQwAAAA?w=289&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7","KKR":"https://th.bing.com/th/id/OIP.0Qy5xuN_RR77ChrUv_C_sQHaFj?w=239&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7","GT":"https://th.bing.com/th/id/OIP.DXNDJzjBE_PWMH1OG38uvgHaFS?w=253&h=181&c=7&r=0&o=5&dpr=1.3&pid=1.7"}
export default function Predict() {
  // state to store the value of the country
  const[img1,setImg1]=useState("");
  const[img2,setImg2]=useState("");
  const [finalimg,setFinalimg]=useState("");
  const [dataresult,setDataresult]=useState("");
  const[display,setDisplay]=useState(false);
  const [tosswinner,setTosswinner]=useState();
  const[tossdecision,setTossDecision]=useState();
  const [country, setCountry] = useState([]);
  const[team1,setTeam1]=useState([]);
  const[team2,setTeam2]=useState([]);
  const[country2,setCountry2]=useState();
  const[index1,setIndex1]=useState(0);
  const[index2,setIndex2]=useState([]);
  const [venue1,setVenue1]=useState([]);
  const [array,setArray]=useState([]);
  const [selectedLocalPlayers, setSelectedLocalPlayers] = useState([]);
    const [selectedOverseasPlayers, setSelectedOverseasPlayers] = useState([]);
    const maxLocalSelections = 8;
    const maxOverseasSelections = 4;
  const [enabler,setEnabler]=useState(false)
  const [selectedLocalPlayers2, setSelectedLocalPlayers2] = useState([]);
    const [selectedOverseasPlayers2, setSelectedOverseasPlayers2] = useState([]);
    const maxLocalSelections2 = 8;
    const maxOverseasSelections2 = 4;
  useEffect(()=>{
    console.log(dataresult);
  },[dataresult])
  useEffect(() => {
    console.log(array); // Log the updated array state
  }, [array]); // Trigger useEffect when form state changes
  const enable=(e)=>{
    e.preventDefault();
    setImg1(dictionary[team1])
    setEnabler(true);
  }
  const submitForm = (e) => {
    e.preventDefault();
    setArray({
      ...array,
      'Team1': team1,
      'Team2': team2,
      'Venue': venue[venue1].name,
      'TossDecision': tossdecision,
      'TossWinner': tosswinner
    });
  }
  const calc=(e)=>{
    e.preventDefault()
    for (let index = 0; index < teams.length; index++) {
      if(teams[index].name===team2){
        console.log(team2+' matches with '+teams[index])
        setIndex2(index);
      }
    setImg2(dictionary[team2]);
    }
  }
  const handleLocalPlayerSelection = (e) => {
    const playerName = e.target.id;
    const isChecked = e.target.checked;

    if (isChecked) {
        // If the player is being selected
        if (selectedLocalPlayers.length < maxLocalSelections) {
            setSelectedLocalPlayers([...selectedLocalPlayers, playerName]);
        } else {
            e.preventDefault(); // Prevent selecting more than the limit
        }
    } else {
        // If the player is being unselected
        setSelectedLocalPlayers(selectedLocalPlayers.filter(player => player !== playerName));
    }
};
const handleLocalPlayerSelection2 = (e) => {
  const playerName = e.target.id;
  const isChecked = e.target.checked;

  if (isChecked) {
      // If the player is being selected
      if (selectedLocalPlayers2.length < maxLocalSelections2) {
          setSelectedLocalPlayers2([...selectedLocalPlayers2, playerName]);
      } else {
          e.preventDefault(); // Prevent selecting more than the limit
      }
  } else {
      // If the player is being unselected
      setSelectedLocalPlayers2(selectedLocalPlayers2.filter(player => player !== playerName));
  }
};
const handleOverseasPlayerSelection = (e) => {
  const playerName = e.target.id;
  const isChecked = e.target.checked;

  if (isChecked) {
      // If the player is being selected
      if (selectedOverseasPlayers.length < maxOverseasSelections) {
          setSelectedOverseasPlayers([...selectedOverseasPlayers, playerName]);
      } else {
          e.preventDefault(); // Prevent selecting more than the limit
      }
  } else {
      // If the player is being unselected
      setSelectedOverseasPlayers(selectedOverseasPlayers.filter(player => player !== playerName));
  }
};
const handleOverseasPlayerSelection2 = (e) => {
  const playerName = e.target.id;
  const isChecked = e.target.checked;

  if (isChecked) {
      // If the player is being selected
      if (selectedOverseasPlayers2.length < maxOverseasSelections2) {
          setSelectedOverseasPlayers2([...selectedOverseasPlayers2, playerName]);
      } else {
          e.preventDefault(); // Prevent selecting more than the limit
      }
  } else {
      // If the player is being unselected
      setSelectedOverseasPlayers2(selectedOverseasPlayers2.filter(player => player !== playerName));
  }
};
  const predictform=(e)=>{
    e.preventDefault();
    fetch("http://localhost:8082/demo",{
      method:'POST',body:JSON.stringify(array),
      headers:{
        'Content-Type':'application/json'
    }
    })
    .then((res)=>res.json())
    .then((data)=>{setDataresult(data.Result)
      setFinalimg(dictionary2[data.Result])
      setDisplay(true)
      console.log(data.Result)
    })
    .catch((err)=>console.log(err))
  }
  return (
    <>
    <div className='navbar'>
        <ul>
          <li><a title='this is about the page'>ABOUT US</a></li>
          <li><a title='to contact the owner of this page contact to +91 9849738965'>CONTACT US</a></li>
          <li>OPTIONS</li>
        </ul>
        <co>
        IplPredictor.com</co>
        <img src='https://th.bing.com/th/id/OIP.PPzJBlQhMrE1wrd1gVaWGAHaEH?w=325&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7' className='logo'></img>
    </div>
    <div className="App">
    <form>
        <center>
            <label for='Team1'>Select Home team:-</label>
      {/* 1st DropDown */}
      {/* 1st DropDown */}
      <select
        name='team1'
        value={country}
        onChange={(e) => {
          console.log(e.target.value);
          console.log(countries[e.target.value].name);
          setIndex1(e.target.value);
          setDataresult('')
          setDisplay(false)
          setEnabler(false)
          setTeam1(countries[e.target.value].name);
          setCountry([e.target.value]);
        }}
      >
        {countries.map((item, index) => {
          return (
            <option key={index} value={index}>
              {item.name}
            </option>
          );
        })}
      </select>
      <button className='team1' onClick={enable}>Select playing XI</button>
      {/* 2nd DropDown */}
      <label for='team2'>Select Away team:-</label>
      <select className='team2' name='team2' onChange={(e)=>{
        // console.log(index1,e.target.value)
        console.log(countries[index1].cities[e.target.value])
        setDataresult('')
        setDisplay(false)
        setTeam2(countries[index1].cities[e.target.value])
      }}>
        {countries[country] &&
          countries[country].cities.map((item, index) => {
            return <option value={index} id={item}>{item}</option>;
          })
          }
      </select>
      <button onClick={calc}>Select playing XI</button>
      <br/>
      {enabler &&<>
      <img src={img1} className='logop'></img>
      <radio className='team1players' name='team1players'>
        {teams[country] &&
            teams[country].cities.map((item, index) => {
              return <label className='team1players'><input  type='radio' id={item} name='team1players' onChange={handleLocalPlayerSelection} disabled={selectedLocalPlayers.length >= maxLocalSelections && !selectedLocalPlayers.includes(item)} checked={selectedLocalPlayers.includes(item)} />{item}{selectedLocalPlayers.includes(item) ? <span className="tick">&#10003;</span> : <span className="cross">&#10005;</span>} {/* Checkmark or cross mark */}<br/></label>;
            })
            }
      </radio>
      <radio className='team1players' name='team1players'>
        {overseasteams[country] &&
            overseasteams[country].cities.map((item, index) => {
              return <label className='team1players'><input  type='radio' id={item} name='team1players' onChange={handleOverseasPlayerSelection} disabled={selectedOverseasPlayers.length >= maxOverseasSelections && !selectedOverseasPlayers.includes(item)} checked={selectedOverseasPlayers.includes(item)} />{item}{selectedOverseasPlayers.includes(item) ? <span className="tick">&#10003;</span> : <span className="cross">&#10005;</span>}<FontAwesomeIcon icon={faPlane} /> {/* Checkmark or cross mark */}<br/></label>;
            })
            }
      </radio><p className='team1players'> &#10003;Indicates selected<br/>&#10005;Indicates Not selected</p></>}
      <img src={img2} className='logop'></img>
      <radio className='team2players' name='team2players'>
        {teams[index2] &&
            teams[index2].cities.map((item, index) => {
              return <label className='team2players'><input  type='radio' id={item} name='team1players' onChange={handleLocalPlayerSelection2} disabled={selectedLocalPlayers2.length >= maxLocalSelections2 && !selectedLocalPlayers2.includes(item)} checked={selectedLocalPlayers2.includes(item)} />{item}{selectedLocalPlayers2.includes(item) ? <span className="tick">&#10003;</span> : <span className="cross">&#10005;</span>} {/* Checkmark or cross mark */}<br/></label>;
            })
            }
      </radio>
      <p className='team2players'>{team2} Overseas Players</p>
      <radio className='team2players' name='team2players'>
        {overseasteams[index2] &&
            overseasteams[index2].cities.map((item, index) => {
              return <label className='team2players'><input  type='radio' id={item} name='team1players' onChange={handleOverseasPlayerSelection2} disabled={selectedOverseasPlayers2.length >= maxOverseasSelections2 && !selectedOverseasPlayers2.includes(item)} checked={selectedOverseasPlayers2.includes(item)} />{item}{selectedOverseasPlayers2.includes(item) ? <span className="tick">&#10003;</span> : <span className="cross">&#10005;</span> }<FontAwesomeIcon icon={faPlane} /> {/* Checkmark or cross mark */}<br/></label>;
            })
            }
      </radio>
      <label for='Venue'>Select Venue:-</label>
      <select className='Venue'
      name='venue'
      value={venue1}
      onChange={(e) => {
      //   console.log(e.target.value);
      setDataresult('')
      setDisplay(false)
        setVenue1([e.target.value]);
      }}
    >
      {venue.map((item, index) => {
        return (
          <option key={index} value={index} name={item.name}>
            {item.name}
          </option>
        );
      })}
    </select>
    <br/>
    <label for='toss_winner'>Toss Winner:-</label>
    <select className='toss_winner' name='toss_winner' onChange={(e)=>{
      setDataresult('')
      setDisplay(false)
        setTosswinner(e.target.value);
    }}>
        <option value='NULL'>N-A</option>
        <option value={team1}>{team1}</option>
        <option value={team2}>{team2}</option>
    </select>
    <br/>
    <label for='toss_select'>Toss Decision:-</label>
    <select className='toss_select' name='toss_select' onChange={(e)=>{
      setDataresult('')
      setDisplay(false)
        setTossDecision(e.target.value);
    }}>
        <option value='NULL'>N-A</option>
        <option value='bat'>bat</option>
        <option value='field'>field</option>
    </select>
    <br/>
    <button onClick={submitForm}>Predict</button>
    <button onClick={predictform} >Get result</button>
    <br/>
    <a href='/History'>Click here to check previous trends</a>
    {display &&<><p>Predicted Winner is {dataresult}<img src={finalimg} className='logop'></img></p></>}
      </center>
      </form>
    </div>
  </>
  );
}
