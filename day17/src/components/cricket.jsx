import React, {useState} from 'react'
const Cricket = () => {
    const[runs, setRuns] = useState(0);
    const[wickets, setWickets] = useState(0);
    const handleSix = () => {
        setRuns(runs + 6);
    }
    const handleFour = () => {
        setRuns(runs + 4);
    }
    const handleThree = () => {
        setRuns(runs + 3);
    }
    const handleTwo = () => {
        setRuns(runs + 2);
    }
    const handleOne = () => {
        setRuns(runs + 1);
    }
    const handleWickets = () => {
        setWickets(wickets + 1);
    }
  return (
    <>
    <h1>Score : {runs} / {wickets}</h1>
    <div>
        <button onClick = {handleSix}>Six</button>
        <button onClick = {handleFour}>Four</button>
        <button onClick = {handleThree}>Three</button>
        <button onClick = {handleTwo}>Two</button>
        <button onClick = {handleOne}>One</button>
        <button onClick = {handleWickets}>wickets</button>
    </div>
    </>
  )
}

export default Cricket