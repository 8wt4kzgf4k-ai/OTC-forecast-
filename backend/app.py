from flask import Flask, request, jsonify
from collector import latest_prices, start_collector
from forecast import generate_forecast
from threading import Thread
from datetime import datetime, timezone

app = Flask(__name__)

# Start collector in background
collector_thread = Thread(target=start_collector, daemon=True)
collector_thread.start()

@app.route("/forecast")
def forecast():
    pair = request.args.get("pair", "EURUSD_otc")
    prices = latest_prices.get(pair, [])
    
    forecast_data = generate_forecast(prices)
    forecast_data["timestamp"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    
    return jsonify(forecast_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
