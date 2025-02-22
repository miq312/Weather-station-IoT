import React from "react";
import TemperatureDisplay from "./TemperatureDisplay";
import TemperatureChart from "./TemperatureChart";

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
