import React, { useState,useEffect } from 'react'
import axios from 'axios';
const Worldcup = () => {
    const ptable={2023:"https://www.espncricinfo.com/series/indian-premier-league-2023-1345038/points-table-standings",
    2022:"https://www.espncricinfo.com/series/indian-premier-league-2022-1298423/points-table-standings",
    2021:"https://www.espncricinfo.com/series/ipl-2021-1249214/points-table-standings",
    2020:"https://www.espncricinfo.com/series/ipl-2020-21-1210595/points-table-standings",
    2019:"https://www.espncricinfo.com/series/ipl-2019-1165643/points-table-standings",
    2018:"https://www.espncricinfo.com/series/ipl-2018-1131611/points-table-standings",
    2017:"https://www.espncricinfo.com/series/ipl-2017-1078425/points-table-standings",
    2016:"https://www.espncricinfo.com/series/ipl-2016-968923/points-table-standings",
    2015:"https://www.espncricinfo.com/series/pepsi-indian-premier-league-2015-791129/points-table-standings",
    2014:"https://www.espncricinfo.com/series/pepsi-indian-premier-league-2014-695871/points-table-standings",
    2013:"https://www.espncricinfo.com/series/pepsi-indian-premier-league-2014-695871/points-table-standings",
    2012:"https://www.espncricinfo.com/series/indian-premier-league-2012-520932/points-table-standings",
    2011:"https://www.espncricinfo.com/series/indian-premier-league-2011-466304/points-table-standings",
    2010:"https://www.espncricinfo.com/series/indian-premier-league-2009-10-418064/points-table-standings",
    2009:"https://www.espncricinfo.com/series/indian-premier-league-2009-374163/points-table-standings",
    2008:"https://www.espncricinfo.com/series/indian-premier-league-2007-08-313494/points-table-standings"}
    const[pointstable,setPointstable]=useState(false);
    const[results,setResults]=useState(false);
    const[stats,setStats]=useState(false);
    const[videos,setVideos]=useState(false);
    const[news,setNews]=useState(false);
    const[thisyear,setThisyear]=useState(0);
    const handleScrapeTable = async () => {
        try {
            const url = ptable[thisyear]; // Assuming ptable[thisyear] contains the URL
            console.log(url);

          const response = await axios.post("http://localhost:8082/year",{url});
          setTableData(response.data.tableData);
        } catch (error) {
          console.error('Error scraping table:', error);
        }
      };
    
    const enabletable=(e)=>{
        e.preventDefault();
        setPointstable(true);
        setStats(false);
        setVideos(false);
        setNews(false);
        setResults(false);
        fetchData();
    }
    const enableresults=(e)=>{
        e.preventDefault();
        setResults(true);
        setPointstable(false);
        setStats(false);
        setVideos(false);
        setNews(false);
    }
    const enablestats=(e)=>{
        e.preventDefault();
        setPointstable(false);
        setStats(true);
        setVideos(false);
        setNews(false);
        setResults(false);
    }
    const enablenews=(e)=>{
        e.preventDefault();
        setPointstable(false);
        setStats(false);
        setVideos(false);
        setNews(true);
        setResults(false);
    }
    const enablevideo=(e)=>{
        e.preventDefault();
        setPointstable(false);
        setStats(false);
        setVideos(true);
        setNews(false);
        setResults(false);
    }
    const setyear=(e)=>{
        e.preventDefault();
        setThisyear(e.target.value);
    }
    const [tableData, setTableData] = useState([]);
    const fetchData = async () => {
        try {
            const response = await axios.get("http://localhost:8080/year");
            setTableData(response.data); // Assuming the response is an array of data
            console.log(response.data);
        } catch (error) {
            console.error('Error fetching data:', error);
            alert('Unable to process the data right now , for the selected year please try later')
        }
    };
    const [resultdata, setResultdata] = useState([]);

    // useEffect(() => {
    //   handleScraperesults();
    // }, []); // Empty dependency array ensures the effect runs only once after initial render

    const handleScraperesults = async () => {
        try {
            const response = await axios.get("http://localhost:8080/results");
            setResultdata(response.data); // Assuming the response is an array of data
            console.log(response.data);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };
  return (
    <>
    <div className='navbar'>
        <ul>
            <label for='year-table' >Select year:-</label>
            <select className='year-table' onChange={setyear}>
                <option value={0}>N-A</option>
                <option value={2024}>2024</option>
                <option value={2023}>2023</option>
                <option value={2022}>2022</option>
                <option value={2021}>2021</option>
                <option value={2020}>2020</option>
                <option value={2019}>2019</option>
                <option value={2018}>2018</option>
                <option value={2017}>2017</option>
                <option value={2016}>2016</option>
                <option value={2015}>2015</option>
                <option value={2014}>2014</option>
                <option value={2013}>2013</option>
                <option value={2012}>2012</option>
                <option value={2011}>2011</option>
                <option value={2010}>2010</option>
                <option value={2009}>2009</option>
                <option value={2008}>2008</option>
                
            </select>
          <li><a title={'Check match fixtures and results of '+thisyear} onClick={enableresults} className='hover-effect'>Check previous results</a></li>
          <li><a title={'Check Points Table of '+thisyear} onClick={enabletable} className='hover-effect'>Points Table</a></li>
          <li><a title={'Check videos in '+thisyear} className='hover-effect'>Videos</a></li>
          <li><a title={'Check Stats of '+thisyear} className='hover-effect'>Stats</a></li>
          <li><a title={'News in '+thisyear} className='hover-effect' href='https://www.cricbuzz.com/cricket-news/'> News</a></li>
        </ul>
        <co>
        IplPredictor.com</co>
        <img src='data:image/jpeg;base64,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' className='logo'></img>
    </div>
    <div className='Worldcup'>
        {pointstable &&<>
        <div className='display-table'>
        {/*
            <h2>Points Table</h2>
            <table className='points table'>
                <thead>
                    <tr>
                        <th>No.</th>
                        <th>Team</th>
                        <th>P</th>
                        <th>W</th>
                        <th>L</th>
                        <th>Pts</th>
                        <th>NRR</th>
                    </tr>
                </thead>
                <tbody>
                    {tableData.map((dataItem, index) => (
                        <tr key={index}>
                            <td>{dataItem.sno}</td>
                            <td>{dataItem.Team}</td>
                            <td>{dataItem.matches}</td>
                            <td>{dataItem.won}</td>
                            <td>{dataItem.lost}</td>
                            <td>{dataItem.Pts}</td>
                            <td>{dataItem.NRR}</td>
                        </tr>
                    ))}
                </tbody>
            </table> */}
            <br/><button onClick={handleScrapeTable}>Scrape Table</button><br/>
            <h2>POINTS TABLE of year {thisyear}</h2>
            <table>
        <tbody>
          {tableData.map((row, rowIndex) => {
            // Conditionally render alternate rows
            if (rowIndex % 2 !== 0) {
              return (
                <tr key={rowIndex}>
                  {row.map((cell, cellIndex) => (
                    <td key={cellIndex}>{cell}</td>
                  ))}
                </tr>
              );
            } else {
              return null; // Skip rendering for odd rows
            }
          })}
        </tbody>
      </table>
        </div>
        </> }
        <br/>
        {results &&<>
        <div className='result-table'>
            <button onClick={handleScraperesults}>Show results</button><br/>
            <h2> Results of IPL {thisyear}</h2>
            <table className='points table'>
                <thead>
                    <tr>
                        <th>Match No.</th><th>Date</th><th>Home team</th><th>Away Team</th><th>City</th><th>Stadium</th><th>Toss</th>
                        <th>Result</th>
                        <th>Won By</th>
                    </tr>
                </thead>
                <tbody>
                    {resultdata.map((dataItem, index) => (
                        <tr key={index}>
                          
                            <td>{dataItem.match_no}</td>
                            <td>{dataItem.date_of_match}</td>
                            <td>{dataItem.Away_team}</td>
                            <td>{dataItem.Home_team}</td>
                            <td>{dataItem.city}</td>
                            <td>{dataItem.venue}</td>
                            <td>{dataItem.toss_winner}</td>
                            <td>{dataItem.winner}</td>
                            <td>{dataItem.result}+{dataItem.result_margin}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
        </>}
        {news && <>
        <div className='news-table'>

        </div>
        </>}
        {videos && <>
        <div className='video-table'>

        </div>
        </>}
        {stats && <>
        <div className='stats-table'>

        </div>
        </>}
    </div>
    </>
  )
}

export default Worldcup