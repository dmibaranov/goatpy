from time import sleep

from goatpy import start_telnet_manhole


if __name__ == '__main__':
    a = 1
    start_telnet_manhole(port=8081, username='admin', password='admin')
    while True:
        sleep(1)
        print a
