import os
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# Store the latest reading
latest_reading = {
    "temperature": 0.0,
    "humidity": 0.0,
    "timestamp": ""
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update():
    """
    Endpoint for ESP32 to POST temperature data.
    Expected JSON: {"temperature": 25.5, "humidity": 60.0}
    """
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    temp = data.get('temperature')
    hum = data.get('humidity')
    
    if temp is None:
        return jsonify({"error": "Temperature missing"}), 400
    
    timestamp = time.strftime('%H:%M:%S')
    
    reading = {
        "temperature": temp,
        "humidity": hum if hum is not None else 0.0,
        "timestamp": timestamp
    }
    
    # Broadcast to all connected web clients
    socketio.emit('new_reading', reading)
    
    return jsonify({"status": "success", "received": reading}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, debug=False, host='0.0.0.0', port=port)
