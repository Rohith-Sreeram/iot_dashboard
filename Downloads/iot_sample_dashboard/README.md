# IoT Temperature Dashboard (ESP32 + Flask)

A premium, real-time dashboard for monitoring ESP32 temperature and humidity data.

## Features
- **Real-time Updates**: Uses WebSockets (Flask-SocketIO) for instant data delivery.
- **Data Visualization**: Live charts powered by Chart.js.
- **Premium Design**: Modern UI with glassmorphism, dark mode, and smooth animations.
- **Simulated Testing**: Includes a Python script to test the dashboard without physical hardware.

## Quick Start (Local Testing)

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask Server**:
   ```bash
   python app.py
   ```
   The dashboard will be available at `http://127.0.0.1:5000`.

3. **Run the Simulator** (in a new terminal):
   ```bash
   python simulate_esp32.py
   ```
   You will see temperature readings appearing on the dashboard in real-time.

## Hardware Setup (ESP32)

1. Open `esp32_code.ino` in the Arduino IDE.
2. Update `ssid`, `password`, and `serverName` (use your computer's local IP).
3. Connect a DHT11 or DHT22 sensor to Pin 4.
4. Upload the code to your ESP32.

## Technologies Used
- **Backend**: Flask, Flask-SocketIO
- **Frontend**: Vanilla JS, Chart.js, CSS3 (Glassmorphism)
- **Hardware Integration**: HTTP POST (REST API)
