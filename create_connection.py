import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    host = 'localhost'
    port = 5000
    
    result = s.connect_ex((host, port))
    if result == 0:
        print("Port is open")
    print(f"Result is {result}")
    s.close()

if __name__ == '__main__':
    main()