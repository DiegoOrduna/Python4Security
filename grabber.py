import socket


class Grabber:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(1)
        self.socket.connect((ip, port))

    def read(self, length=2048):
        # get banner
        banner = self.socket.recv(length)
        return banner

    def close(self):
        self.socket.close()


if __name__ == "__main__":
    grabber = Grabber("192.168.100.99", 23)
    print(grabber.read())
    grabber.close()
