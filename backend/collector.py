from playwright.sync_api import sync_playwright
import time
from datetime import datetime, timezone

latest_prices = {}

PAIRS = ["EURUSD_otc", "GBPUSD_otc", "USDJPY_otc"]
PRICE_SELECTOR = "span.price-value"  # Replace with actual selector
SESSION_COOKIES = []

def start_collector():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for cookie in SESSION_COOKIES:
            page.context.add_cookies([cookie])

        page.goto("https://pocketoption.com")
        page.wait_for_timeout(5000)

        while True:
            for pair in PAIRS:
                try:
                    price_text = page.text_content(PRICE_SELECTOR)
                    price = float(price_text.replace(",", "").strip())
                    tick_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

                    if pair not in latest_prices:
                        latest_prices[pair] = []

                    latest_prices[pair].append({"price": price, "timestamp": tick_time})

                    if len(latest_prices[pair]) > 1000:
                        latest_prices[pair] = latest_prices[pair][-1000:]
                except Exception as e:
                    print(f"Error reading {pair}: {e}")

            time.sleep(1)
