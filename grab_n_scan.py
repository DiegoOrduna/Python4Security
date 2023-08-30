from port_scanner import Scanner
from grabber import Grabber
from utils import timefunc


@timefunc
def main():
    ip = "192.168.100.99"
    scanner = Scanner(ip)
    scanner.scan(1, 150)
    for port in scanner.open_ports:
        try:
            grabber = Grabber(ip, port)
            print(grabber.read())
            grabber.close()
        except Exception as e:
            print(f"Port {port} Error!\n{e}")


if __name__ == "__main__":
    main()
