def generate_forecast(ticks):
    if not ticks or len(ticks) < 3:
        return {
            "1m": {"direction": "UP", "confidence": 50, "momentum": "Neutral"},
            "3m": {"direction": "UP", "confidence": 50, "momentum": "Neutral"},
            "5m": {"direction": "UP", "confidence": 50, "momentum": "Neutral"},
        }

    last = ticks[-1]["price"]
    prev = ticks[-2]["price"]
    prev2 = ticks[-3]["price"]

    velocity = last - prev
    prev_velocity = prev - prev2
    acceleration = velocity - prev_velocity

    direction = "UP" if velocity > 0 else "DOWN"
    confidence = min(99, abs(velocity) * 100)

    if direction == "UP":
        if acceleration > 0:
            momentum = "Accelerating UP"
        elif acceleration < 0:
            momentum = "Slowing UP"
        else:
            momentum = "Neutral"
    else:
        if acceleration < 0:
            momentum = "Accelerating DOWN"
        elif acceleration > 0:
            momentum = "Slowing DOWN"
        else:
            momentum = "Neutral"

    return {
        "1m": {"direction": direction, "confidence": confidence, "momentum": momentum},
        "3m": {"direction": direction, "confidence": max(confidence - 5, 0), "momentum": momentum},
        "5m": {"direction": direction, "confidence": max(confidence - 10, 0), "momentum": momentum},
    }
