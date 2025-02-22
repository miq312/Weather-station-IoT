import machine
import onewire
import ds18x20
import time

class TemperatureSensor:
    def __init__(self, pin=4):
        self.sensor_pin = machine.Pin(pin)
        self.ds_sensor = ds18x20.DS18X20(onewire.OneWire(self.sensor_pin))
        self.roms = self.ds_sensor.scan()
        if not self.roms:
            print("No DS18B20 sensor found.")
            raise SystemExit

    def read_temperature(self):
        self.ds_sensor.convert_temp()
        time.sleep(1)
        return self.ds_sensor.read_temp(self.roms[0])
