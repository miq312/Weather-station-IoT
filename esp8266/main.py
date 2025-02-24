import network
import time
from mqtt import MQTTHandler
from sensor import TemperatureSensor

SSID = '...'
PASSWORD = '...'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

if not wlan.isconnected():
    print('\nConnecting to Wi-Fi...')
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        time.sleep(1)
        print(".")
print('Connected to Wi-Fi')
print('IP Address:', wlan.ifconfig()[0])

mqtt_handler = MQTTHandler()
mqtt_handler.connect()
sensor = TemperatureSensor()

while True:
    temperature = sensor.read_temperature()
    mqtt_handler.publish_temperature(temperature)
    time.sleep(5)

