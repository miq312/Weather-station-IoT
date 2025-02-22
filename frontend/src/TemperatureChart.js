import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';
import axios from 'axios';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const TemperatureChart = () => {
  const [temperatureData, setTemperatureData] = useState([]);
  
  useEffect(() => {
    // Funkcja do pobierania danych z backendu
    const fetchTemperatureData = () => {
      axios.get('http://localhost:5000/api/temperature')
        .then((response) => {
          // Pobierz pierwsze dane, aby stworzyć wykres
          const newTemperatureData = response.data.map(item => ({
            timestamp: item.timestamp,
            temperature: item.temperature
          }));

          // Uaktualnij stan wykresu
          setTemperatureData(newTemperatureData);
        })
        .catch((error) => {
          console.error("Error fetching temperature data: ", error);
        });
    };

    // Pobierz dane od razu po załadowaniu komponentu
    fetchTemperatureData();

    // Aktualizuj dane co 10 sekund
    const intervalId = setInterval(fetchTemperatureData, 10000);

    return () => clearInterval(intervalId); // Usuwanie interwału po zakończeniu działania komponentu
  }, []);

  const chartData = {
    labels: temperatureData.map((item) => item.timestamp), // Pobierz dane z timestampów
    datasets: [
      {
        label: 'Temperatura',
        data: temperatureData.map((item) => item.temperature), // Temperatura
        fill: false,
        borderColor: 'rgba(75, 192, 192, 1)',
        tension: 0.1,
      },
    ],
  };

  return (
    <div>
      <h2>Wykres Temperatury</h2>
      <Line data={chartData} />
    </div>
  );
};

export default TemperatureChart;
