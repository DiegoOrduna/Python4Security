import socket
from utils import timefunc


class Scanner:
    def __init__(self, ip):
        self.ip = ip
        self.open_ports = []

    def __repr__(self):
        return f"Scanner: {self.ip}"

    def scan(self, lowerport, upperport):
        for port in range(lowerport, upperport + 1):
            if self.is_open(port):
                print(f"Port {port} is open")
                self.open_ports.append(port)

    def is_open(self, port):
        # print(f"Checking port {port}")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        result = s.connect_ex((self.ip, port))
        s.close()
        return result == 0

    def write(self, filepath):
        with open(filepath, "w") as f:
            for port in self.open_ports:
                f.write(f"{port}\n")


@timefunc
def main():
    ip = "localhost"
    scanner = Scanner(ip)
    print(scanner.__repr__())
    scanner.scan(1, 100)
    scanner.write("./open_ports.txt")


if __name__ == "__main__":
    main()
