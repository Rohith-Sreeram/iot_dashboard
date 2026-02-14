/*
  ESP32 Temperature & Humidity Sender
  This sketch sends data to the Flask IoT Dashboard.
  
  Dependencies:
  - DHT sensor library (by Adafruit)
  - HTTPClient (built-in)
  - WiFi (built-in)
*/

#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>

// Replace with your network credentials
const char* ssid     = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";

// Replace with your computer's IP address and Flask port
// Example: "http://192.168.1.10:5000/update"
const char* serverName = "http://YOUR_COMPUTER_IP:5000/update";

#define DHTPIN 4     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11 // DHT 11 (or DHT22)

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  
  dht.begin();

  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  if(WiFi.status()== WL_CONNECTED){
    HTTPClient http;

    http.begin(serverName);
    http.addHeader("Content-Type", "application/json");

    float t = dht.readTemperature();
    float h = dht.readHumidity();

    if (isnan(h) || isnan(t)) {
      Serial.println("Failed to read from DHT sensor!");
      return;
    }

    // Create JSON data
    String httpRequestData = "{\"temperature\":" + String(t) + ", \"humidity\":" + String(h) + "}";
    
    int httpResponseCode = http.POST(httpRequestData);
    
    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);
    
    http.end();
  }
  else {
    Serial.println("WiFi Disconnected");
  }
  
  // Send data every 5 seconds
  delay(5000);
}
