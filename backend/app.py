##################################### TEST APP ###################################

from flask import Flask, jsonify
from flask_cors import CORS
import paho.mqtt.client as mqtt
import sqlite3

app = Flask(__name__)
CORS(app)

def create_db():
    conn = sqlite3.connect('temperature_data.db')
    c = conn.cursor()
    c.execute(
        '''CREATE TABLE IF NOT EXISTS temperature (id INTEGER PRIMARY KEY, value REAL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def save_to_db(temperature):
    conn = sqlite3.connect('temperature_data.db')
    c = conn.cursor()
    c.execute('''INSERT INTO temperature (value) VALUES (?)''', (temperature,))
    conn.commit()
    conn.close()

MqttTopic = "esp_temperature"

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with result code {rc}")
    client.subscribe(MqttTopic)
    print(f"Subscribe topic: {MqttTopic}")


def on_message(client, userdata, msg):
    try:
        temperature = float(msg.payload.decode())
        print(f"Temp: {temperature}")
        save_to_db(temperature)
    except ValueError:
        print(f"Error with message: {msg.payload.decode()}")




client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.enable_logger()
client.connect("192.168.1.62", 1883, 60)
client.loop_start()


@app.route('/api/temperature', methods=['GET'])
def get_temperature():
    conn = sqlite3.connect('temperature_data.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM temperature ORDER BY rowid DESC LIMIT 100''')
    rows = c.fetchall()
    conn.close()

    return jsonify([{"temperature": row[1], "timestamp": row[2]} for row in rows])


if __name__ == '__main__':
    create_db()
    app.run(host='0.0.0.0', debug=True)
