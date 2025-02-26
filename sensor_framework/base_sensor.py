from abc import ABC, abstractmethod

class BaseSensor(ABC):
    """Abstract base class for all sensors"""

    def __init__(self, name):
        self.name = name
        self.connected = False

    @abstractmethod
    def connect(self):
        """Establish connection to the sensor"""
        pass

    @abstractmethod
    def start_stream(self):
        """Start data streaming"""
        pass

    @abstractmethod
    def process_data(self, data):
        """Process incoming data"""
        pass

    @abstractmethod
    def stop_stream(self):
        """Stop data streaming"""
        pass
