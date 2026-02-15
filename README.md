# OTC Forex Forecast

## Overview
This project provides **real-time OTC Forex forecasts** for 1-minute, 3-minute, and 5-minute timeframes. It uses live price data from Pocket Option and calculates **direction, momentum/reversal, and confidence levels**. The frontend displays forecasts with color coding, background changes, and a **15-second flash** for new updates. All timestamps are in **UTC**.

---

## Features
- Live **1m / 3m / 5m forecasts** for selected pairs
- Momentum / Reversal detection:
  - Accelerating Up/Down
  - Slowing Up/Down
  - Neutral
- **Independent 15-second flash** for each timeframe when a new forecast is available
- Color-coded text for direction (green/up, red/down, orange/neutral)
- Background changes based on 1-minute forecast
- UTC timestamps for all forecasts
- OTC pairs appear at the top of the selector

---

## Folder Structure
