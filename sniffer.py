import signal
import socket
from capture import PCAPFile

def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    pcap = PCAPFile('packets.pcap')
    while True:
        try:
            raw_data, addr = conn.recvfrom(65535)
            pcap.write(raw_data)
        except KeyboardInterrupt:
            pcap.close()
            print("\nStopped packet capturing")

if __name__ == '__main__':
    main()
