import requests
import time
import random

# The URL where your Flask app is running
# If running locally, this is usually http://127.0.0.1:5000/update
URL = "http://127.0.0.1:5000/update"

print("Starting ESP32 Simulation...")
print(f"Sending data to {URL}")

try:
    while True:
        # Simulate temperature and humidity
        temp = random.uniform(20.0, 30.0)
        hum = random.uniform(40.0, 60.0)
        
        data = {
            "temperature": round(temp, 2),
            "humidity": round(hum, 2)
        }
        
        try:
            response = requests.post(URL, json=data)
            print(f"Sent: {data} | Status Code: {response.status_code}")
        except requests.exceptions.ConnectionError:
            print("Error: Could not connect to Flask app. Is it running?")
        
        # Wait for 2 seconds before next reading
        time.sleep(2)
except KeyboardInterrupt:
    print("\nSimulation stopped.")
