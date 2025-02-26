from sensors.emotibit_sensor import EmotiBitSensor
from sensors.openbci_sensor import OpenBCISensor

class SensorManager:
    def __init__(self):
        self.sensors = []

    def register_sensor(self, sensor):
        """Register a new sensor"""
        self.sensors.append(sensor)

    def connect_all(self):
        """Connect all registered sensors"""
        for sensor in self.sensors:
            sensor.connect()

    def start_all_streams(self):
        """Start data streaming for all sensors"""
        for sensor in self.sensors:
            sensor.start_stream()

    def stop_all_streams(self):
        """Stop all sensor streams"""
        for sensor in self.sensors:
            sensor.stop_stream()
