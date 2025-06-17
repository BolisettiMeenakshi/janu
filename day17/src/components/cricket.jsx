import React, {useState} from 'react'
const cricket = () => {
    const[runs, setRuns] = useState(0);
    const[wickets, setWickets] = useState(0);
    const handleSix = () => {
        setRuns(runs + 6);
    }
    const handleFour = () => {
        setRuns(runs + 4);
    }
    const handleOne = () => {
        setRuns(runs + 1);
    }
    const handleWickets = () => {
        setWickets(wickets + 1)
    }
  return (
    <>
    <h1>Score : {runs} / {wickets}</h1>
    <div>
        <button onClick = {handleSix}>Six</button>
        <button onClick = {handleFour}>Four</button>
        <button onClick = {handleOne}>One</button>
        <button onClick = {handleWickets}>wickets</button>
    </div>
    </>
  )
}

export default cricket