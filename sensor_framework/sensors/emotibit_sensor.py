import socket
import time
from sensor_framework.base_sensor import BaseSensor

BROADCAST_PORT = 12345
DATA_PORT = 3000

class EmotiBitSensor(BaseSensor):
    def __init__(self):
        super().__init__("EmotiBit")
        self.ip_address = None
        self.socket = None

    def discover_emotibit(self, timeout=5):
        """Find EmotiBit on the network using UDP broadcast"""
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.settimeout(timeout)
            sock.sendto(b'EMOTIBIT_DISCOVERY', ('<broadcast>', BROADCAST_PORT))

            try:
                _, addr = sock.recvfrom(1024)
                self.ip_address = addr[0]
                print(f"Discovered EmotiBit at {self.ip_address}")
                return True
            except socket.timeout:
                print("No EmotiBit found.")
                return False

    def connect(self):
        if self.discover_emotibit():
            self.connected = True
        else:
            self.connected = False

    def start_stream(self):
        if not self.connected:
            print("EmotiBit not connected. Cannot start stream.")
            return
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.ip_address, DATA_PORT))
        print(f"EmotiBit streaming from {self.ip_address}:{DATA_PORT}")

    def process_data(self, data):
        print(f"Processing EmotiBit data: {data}")

    def stop_stream(self):
        if self.socket:
            self.socket.close()
        print("EmotiBit streaming stopped.")
