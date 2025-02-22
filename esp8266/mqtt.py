import time
from umqtt.simple import MQTTClient


class MQTTHandler:
    def __init__(self, broker='192.168.1.62', port=1883, topic='esp_temp'):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client = MQTTClient("esp8266", self.broker, port=self.port)

    def connect(self):
        while True:
            try:
                self.client.connect()
                print(f"Connected to MQTT broker: {self.broker}")
                return
            except OSError as e:
                print(f"Connection error: {e}, retrying...")
                time.sleep(5)

    def publish_temperature(self, temperature):
        print(f"Sending temperature: {temperature:.2f}°C")
        self.client.publish(self.topic, str(temperature))