import React from "react";
import TemperatureDisplay from "./components//TemperatureDisplay";
import TemperatureChart from "./components/TemperatureChart";
import './App.css';

function App() {
  return (
    <div className="App">
      <h1>Temperature Dashboard</h1>
      <TemperatureDisplay />
      <TemperatureChart />
    </div>
  );
}

export default App;
