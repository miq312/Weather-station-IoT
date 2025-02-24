import React, { useState, useEffect } from "react";
import axios from "axios";

function TemperatureDisplay() {
  const [temperature, setTemperature] = useState(null);

  useEffect(() => {
    const fetchTemperature = () => {
      axios
        .get("http://192.168.1.62:5000/api/temperature")
        .then((response) => {
          setTemperature(response.data[0]?.temperature);
        })
        .catch((error) => {
          console.error("Error fetching temperature data: ", error);
        });
    };

    fetchTemperature();

    const interval = setInterval(fetchTemperature, 5000); 

    return () => clearInterval(interval); 
  }, []);

  return (
    <div>
      <h2>Current Temperature</h2>
      <p>{temperature ? `${temperature}°C` : "Loading..."}</p>
    </div>
  );
}

export default TemperatureDisplay;
