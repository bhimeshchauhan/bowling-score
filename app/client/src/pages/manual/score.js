import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './score.css';

function Score() {
    const initData = [{
        1: ["-", "-", "-", "-"],
        2: ["-", "-", "-", "-"],
        3: ["-", "-", "-", "-"],
        4: ["-", "-", "-", "-"],
        5: ["-", "-", "-", "-"],
        6: ["-", "-", "-", "-"],
        7: ["-", "-", "-", "-"],
        8: ["-", "-", "-", "-"],
        9: ["-", "-", "-", "-"],
        10: ["-", "-", "-", "-"]
    }]
    const [scorePanel, setScorePanel] = useState([])
    const [data, setData] = useState(initData)
    const [score, setScore] = useState(0)

    const newPlay = (e) => {
        const val = e.target.value;
        setScorePanel([...scorePanel, val])
    }

    useEffect(() => {
        let apiurl = 'http://localhost:8000/api/score'
        let payload = {
            data: scorePanel
        }
        axios.post(apiurl, payload).then((response) => {
            if(response.status === 200) {
                let result = response.data.result[0];
                Object.keys(result).forEach(idx => {
                    if(result[idx] === null) {
                        result[idx] = ['-', '-', '-', '-']
                    }
                });
                setData([result]);
                setScore(response.data.score);
            }
        })
    }, [scorePanel])

    const clear = () => {
        setScorePanel([])
        setData(initData);
        setScore(0);
    }

    return (
        <div className="score">
            <h1 className="title">Bowling Score Card</h1>
            <h2 className="title">Control Panel</h2>
            <div id="buttons" className="buttons">
                <button type="button" onClick={newPlay} value='-'  className="btn btn-primary">Gutter</button>
                <button type="button" onClick={newPlay} value={1} className="btn btn-primary">1</button>
                <button type="button" onClick={newPlay} value={2} className="btn btn-primary">2</button>
                <button type="button" onClick={newPlay} value={3}  className="btn btn-primary">3</button>
                <button type="button" onClick={newPlay} value={4}  className="btn btn-primary">4</button>
                <button type="button" onClick={newPlay} value={5}  className="btn btn-primary">5</button>
                <button type="button" onClick={newPlay} value={6}  className="btn btn-primary">6</button>
                <button type="button" onClick={newPlay} value={7}  className="btn btn-primary">7</button>
                <button type="button" onClick={newPlay} value={8}  className="btn btn-primary">8</button>
                <button type="button" onClick={newPlay} value={9}  className="btn btn-primary">9</button>
                <button type="button" onClick={newPlay} value={10}  className="btn btn-primary">10</button>
                <button type="button" onClick={clear} value={10}  className="btn btn-primary">clear</button>
            </div>
            <div id='scorecard'>
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
                            <td colSpan='3'></td><td id="frame1" colSpan='3'>{data[0][1][0]} {data[0][1][1] !== " " ? ',' : null} {data[0][1][1]}</td>
                            <td colSpan='3'></td><td id="frame2" colSpan='3'>{data[0][2][0]} {data[0][2][1] !== " " ? ',' : null} {data[0][2][1]}</td>
                            <td colSpan='3'></td><td id="frame3" colSpan='3'>{data[0][3][0]} {data[0][3][1] !== " " ? ',' : null} {data[0][3][1]}</td>
                            <td colSpan='3'></td><td id="frame4" colSpan='3'>{data[0][4][0]} {data[0][4][1] !== " " ? ',' : null} {data[0][4][1]}</td>
                            <td colSpan='3'></td><td id="frame5" colSpan='3'>{data[0][5][0]} {data[0][5][1] !== " " ? ',' : null} {data[0][5][1]}</td>
                            <td colSpan='3'></td><td id="frame6" colSpan='3'>{data[0][6][0]} {data[0][6][1] !== " " ? ',' : null} {data[0][6][1]}</td>
                            <td colSpan='3'></td><td id="frame7" colSpan='3'>{data[0][7][0]} {data[0][7][1] !== " " ? ',' : null} {data[0][7][1]}</td>
                            <td colSpan='3'></td><td id="frame8" colSpan='3'>{data[0][8][0]} {data[0][8][1] !== " " ? ',' : null} {data[0][8][1]}</td>
                            <td colSpan='3'></td><td id="frame9" colSpan='3'>{data[0][9][0]} {data[0][9][1] !== " " ? ',' : null} {data[0][9][1]}</td>
                            <td colSpan='3'></td><td id="frame10" colSpan='3'>{data[0][10][0]} {data[0][10][1] !== " " ? ',' : null} {data[0][10][1]}</td>
                        </tr>
                        <tr>
                            <td colSpan='6'id="marker0">{data[0][1][3]}</td>
                            <td colSpan='6'id="marker1">{data[0][2][3]}</td>
                            <td colSpan='6'id="marker2">{data[0][3][3]}</td>
                            <td colSpan='6'id="marker3">{data[0][4][3]}</td>
                            <td colSpan='6'id="marker4">{data[0][5][3]}</td>
                            <td colSpan='6'id="marker5">{data[0][6][3]}</td>
                            <td colSpan='6'id="marker6">{data[0][7][3]}</td>
                            <td colSpan='6'id="marker7">{data[0][8][3]}</td>
                            <td colSpan='6'id="marker8">{data[0][9][3]}</td>
                            <td colSpan='6'id="marker9">{data[0][10][3]}</td>
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
        </div>
    );
}

export default Score;
