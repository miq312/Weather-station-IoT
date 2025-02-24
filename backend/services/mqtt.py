import paho.mqtt.client as mqtt
from database import save_to_db
from config import MQTT_BROKER, MQTT_PORT

mqttTopic = "esp_temperature"

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with result code {rc}")
    client.subscribe(mqttTopic)
    print(f"Subscribe topic: {mqttTopic}")


def on_message(client, userdata, msg):
    try:
        temperature = float(msg.payload.decode())
        print(f"Received temperature: {temperature}")
        save_to_db(temperature)
    except ValueError:
        print(f"Invalid message: {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.enable_logger()
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()