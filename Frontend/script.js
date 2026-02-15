const select = document.getElementById("pairSelect");
const output = document.getElementById("output");
let lastForecast = {};

async function loadForecast(pair) {
  try {
    const response = await fetch(`https://your-railway-app.up.railway.app/forecast?pair=${pair}`);
    const data = await response.json();

    function getClass(direction) {
      if(direction.includes("UP")) return "forecast-up";
      if(direction.includes("DOWN")) return "forecast-down";
      return "forecast-neutral";
    }

    function flashIfChanged(timeframe) {
      if(!lastForecast[timeframe] || lastForecast[timeframe].direction !== data[timeframe].direction) {
        return "flash";
      }
      return "";
    }

    lastForecast = data;

    if(data["1m"].direction.includes("UP")) document.body.style.backgroundColor = "#d4fcd4";
    else if(data["1m"].direction.includes("DOWN")) document.body.style.backgroundColor = "#fcd4d4";
    else document.body.style.backgroundColor = "#fff0d4";

    output.innerHTML = `
      <p class="${getClass(data["1m"].direction)} ${flashIfChanged("1m")}">
        1m: ${data["1m"].direction} (${data["1m"].confidence}%) - ${data["1m"].momentum}
      </p>
      <p class="${getClass(data["3m"].direction)} ${flashIfChanged("3m")}">
        3m: ${data["3m"].direction} (${data["3m"].confidence}%) - ${data["3m"].momentum}
      </p>
      <p class="${getClass(data["5m"].direction)} ${flashIfChanged("5m")}">
        5m: ${data["5m"].direction} (${data["5m"].confidence}%) - ${data["5m"].momentum}
      </p>
      <p>Last updated (UTC): ${data.timestamp}</p>
    `;
  } catch {
    output.innerHTML = "<p style='color:red;'>Error loading forecast</p>";
  }
}

select.addEventListener("change", e => loadForecast(e.target.value));
loadForecast(select.value);
setInterval(() => loadForecast(select.value), 60000);
