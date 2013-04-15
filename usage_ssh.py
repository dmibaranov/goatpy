from time import sleep

from goatpy import start_ssh_manhole


if __name__ == '__main__':
    a = 1
    start_ssh_manhole(port=8022, username='admin', password='admin')
    while True:
        sleep(1)
        print a
