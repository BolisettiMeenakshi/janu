import React, {useState} from 'react'
const Cricket = (props) => {
    console.log("props", props);
    console.log("target = ",props.target );
    const[runs, setRuns] = useState(0);
    const[wickets, setWickets] = useState(0);
    const[balls, setBalls] = useState(0);
    const[Overs, setOvers] = useState(0);
    const[totalOvers, setTotalOvers] = useState(props.overs);
    const[currentOvers, setCurrentOvers] = useState(0);
    const[RemainingOvers, setRemainingOvers] = useState(0);
    const[target, setTarget] = useState(props.target);
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
    const handleDot = () => {
        setRuns(runs + 0);
    }
    const handleWickets = () => {
        if(wickets + 1 === 10)
            alert("All Out")
        setWickets(wickets + 1)
    }
   
    const handleNextOver = () => {
        if(currentOvers < RemainingOvers)
            setCurrentOvers(currentOvers + 1)
    }
    const handleRuns = (run) => {
        if(runs + run >= target)
            alert("Target Chased");
        setRuns(runs + run)
    }
    const handleOvers = (run) => {
        if(runs + run != target)
            alert("Failed to chase target");
        setRuns(Overs )
    };
  return (
    <>
    <h1>Score : {runs} / {wickets}</h1>
    <p>currentOvers : {Overs}.{balls}</p>
    <p>RemaingOvers : {RemainingOvers}</p>
    {

        wickets < 10 && runs < target ?
    <div>
        <button onClick = {handleSix}>Six</button>
        <button onClick = {handleFour}>Four</button>
        <button onClick = {handleThree}>Three</button>
        <button onClick = {handleTwo}>Two</button>
        <button onClick = {handleOne}>One</button>
        <button onClick = {handleDot}>Dot</button>
        <button onClick = {handleWickets}>wickets</button>
    </div>
    :
    <h3>Game Over</h3>
}
    </>
  )
}

export default Cricket