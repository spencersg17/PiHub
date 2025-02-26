# sensor_framework/sensors/__init__.py

from .emotibit_sensor import EmotiBitSensor
from .openbci_sensor import OpenBCISensor

__all__ = ["EmotiBitSensor", "OpenBCISensor"]