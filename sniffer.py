import socket

def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    data = conn.recvfrom(65500)
    print(data)

if __name__ == '__main__':
    main()
