from sensor_framework.sensor_manager import SensorManager
from sensor_framework.sensors.emotibit_sensor import EmotiBitSensor
from sensor_framework.sensors.openbci_sensor import OpenBCISensor
import time

def main():
    manager = SensorManager()

    # Register sensors
    manager.register_sensor(EmotiBitSensor())
    # manager.register_sensor(OpenBCISensor("/dev/ttyUSB0"))

    # Connect sensors
    manager.connect_all()

    # Start streaming
    manager.start_all_streams()

    try:
        while True:
            # Simulate data processing
            for sensor in manager.sensors:
                sensor.process_data("Simulated Data")
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopping all sensors...")
        manager.stop_all_streams()

if __name__ == "__main__":
    main()
