const apiKey = "85343279c8b53dbb03ce487de38a0be9";
const weatherButton = document.getElementById("getWeather");
const resultDiv = document.getElementById("result");

weatherButton.addEventListener("click", () => {
  const city = document.getElementById("city").value.trim();
  if (!city) {
    resultDiv.textContent = "Please enter a city name.";
    return;
  }

  resultDiv.textContent = "Loading weather data...";

  fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`)
    .then((response) => {
      if (!response.ok) {
        throw new Error("City not found. Please check the name and try again.");
      }
      return response.json();
    })
    .then((data) => {
      const { main, weather, wind } = data;
      resultDiv.innerHTML = `
        <h2>Weather in ${city}</h2>
        <p>Temperature: ${main.temp}°C</p>
        <p>Condition: ${weather[0].description}</p>
        <p>Humidity: ${main.humidity}%</p>
        <p>Wind Speed: ${wind.speed} m/s</p>
      `;
    })
    .catch((error) => {
      resultDiv.textContent = error.message;
    });
});
