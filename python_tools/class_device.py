# class_device.py

from datetime import date

class Device:
    """Base class for all devices."""
    def __init__(self, name: str, ip: str | None = None):
        self.name = name
        self.ip = ip
        self.created = date.today()

    def identify(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', ip={self.ip})"

    def connect(self) -> str:
        return f"{self.name} connecting..." if self.ip else f"{self.name} has no IP configured."

class Laptop(Device):
    def __init__(self, name: str, ip: str | None = None, os: str = "Windows"):
        super().__init__(name, ip)
        self.os = os

    def install_app(self, app: str) -> str:
        return f"Installing {app} on {self.name} ({self.os})"

class Router(Device):
    def __init__(self, name: str, ip: str | None = None, ports: int = 4):
        super().__init__(name, ip)
        self.ports = ports

    def route(self, dest_ip: str) -> str:
        return f"{self.name} routing traffic to {dest_ip}"

def demo():
    d1 = Device("Generic Device")
    l1 = Laptop("Dev-Laptop", "192.168.1.50", os="Linux")
    r1 = Router("Edge-Router", "192.168.1.1", ports=8)

    print(d1.identify()); print(d1.connect())
    print(l1.identify()); print(l1.connect()); print(l1.install_app("Wireshark"))
    print(r1.identify()); print(r1.connect()); print(r1.route("8.8.8.8"))

if __name__ == "__main__":
    demo()
