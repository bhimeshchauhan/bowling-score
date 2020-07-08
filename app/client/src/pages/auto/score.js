import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './score.css';

function Score() {
    const[data, setData] = useState([])
    useEffect(() => {
        const getColumnData = async () => {
            return await axios.get('http://localhost:8000/api/score/')
            .then((response) => {
                setData(response.data);
            })
        }
        getColumnData();
    }, []);
    return (
        <div className="score">
            <h1 className="title">Bowling Score Card - CSV</h1>
            {   
                data.map((dataItem, idx) => {
                    let item = dataItem.result
                    let score = dataItem.score
                    Object.keys(item).forEach(idx => {
                        if(item[idx] === null) {
                            item[idx] = ['-', '-', '-', '-']
                        }
                    });
                    return (
                        <div id='scorecard' key={idx}>
                            <table id='scorecardTable' className='scorecard' cellPadding='1' cellSpacing='0'>
                                <tbody>
                                    <tr>
                                        <th colSpan='6'>Frame 1</th>
                                        <th colSpan='6'>Frame 2</th>
                                        <th colSpan='6'>Frame 3</th>
                                        <th colSpan='6'>Frame 4</th>
                                        <th colSpan='6'>Frame 5</th>
                                        <th colSpan='6'>Frame 6</th>
                                        <th colSpan='6'>Frame 7</th>
                                        <th colSpan='6'>Frame 8</th>
                                        <th colSpan='6'>Frame 9</th>
                                        <th colSpan='6'>Frame 10</th>
                                    </tr>
                                    <tr>
                                        <td colSpan='3'></td><td id="frame1" colSpan='3'>{item[1][0]} {item[1][1] !== " " ? ',' : null} {item[1][1]}</td>
                                        <td colSpan='3'></td><td id="frame2" colSpan='3'>{item[2][0]} {item[2][1] !== " " ? ',' : null} {item[2][1]}</td>
                                        <td colSpan='3'></td><td id="frame3" colSpan='3'>{item[3][0]} {item[3][1] !== " " ? ',' : null} {item[3][1]}</td>
                                        <td colSpan='3'></td><td id="frame4" colSpan='3'>{item[4][0]} {item[4][1] !== " " ? ',' : null} {item[4][1]}</td>
                                        <td colSpan='3'></td><td id="frame5" colSpan='3'>{item[5][0]} {item[5][1] !== " " ? ',' : null} {item[5][1]}</td>
                                        <td colSpan='3'></td><td id="frame6" colSpan='3'>{item[6][0]} {item[6][1] !== " " ? ',' : null} {item[6][1]}</td>
                                        <td colSpan='3'></td><td id="frame7" colSpan='3'>{item[7][0]} {item[7][1] !== " " ? ',' : null} {item[7][1]}</td>
                                        <td colSpan='3'></td><td id="frame8" colSpan='3'>{item[8][0]} {item[8][1] !== " " ? ',' : null} {item[8][1]}</td>
                                        <td colSpan='3'></td><td id="frame9" colSpan='3'>{item[9][0]} {item[9][1] !== " " ? ',' : null} {item[9][1]}</td>
                                        <td colSpan='3'></td><td id="frame10" colSpan='3'>{item[10][0]} {item[10][1] !== " " ? ',' : null} {item[10][1]}</td>
                                    </tr>
                                    <tr>
                                        <td colSpan='6'id="marker0">{item[1][3]}</td>
                                        <td colSpan='6'id="marker1">{item[2][3]}</td>
                                        <td colSpan='6'id="marker2">{item[3][3]}</td>
                                        <td colSpan='6'id="marker3">{item[4][3]}</td>
                                        <td colSpan='6'id="marker4">{item[5][3]}</td>
                                        <td colSpan='6'id="marker5">{item[6][3]}</td>
                                        <td colSpan='6'id="marker6">{item[7][3]}</td>
                                        <td colSpan='6'id="marker7">{item[8][3]}</td>
                                        <td colSpan='6'id="marker8">{item[9][3]}</td>
                                        <td colSpan='6'id="marker9">{item[10][3]}</td>
                                    </tr>
                                </tbody>
                            </table>
                            <table id='scorecardTable-score' className='scorecard-score' cellPadding='1' cellSpacing='0'>
                                <tbody>
                                    <tr>
                                        <th colSpan='3'>Score</th>
                                    </tr>
                                    <tr>
                                        <td colSpan='6'id="marker9">{score}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>

                    )
                })
            }
        </div>
    );
}

export default Score;
