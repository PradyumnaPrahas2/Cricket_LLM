import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Predict.css'
const Points = () => {
    const [tableData, setTableData] = useState([]);

    useEffect(() => {
        fetchData();
    }, []); // Empty dependency array ensures the effect runs only once after initial render

    const fetchData = async () => {
        try {
            const response = await axios.get("http://localhost:8080/ipldatas");
            setTableData(response.data); // Assuming the response is an array of data
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    return (
        <div>
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
                            <td>{dataItem.Team1}</td>
                            <td>{dataItem.Team2}</td>
                            <td>{dataItem.Venue}</td>
                            <td>{dataItem.TossWinner}</td>
                            <td>{dataItem.TossDecision}</td>
                            <td>{dataItem.Pts}</td>
                            <td>{dataItem.NRR}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default Points;
