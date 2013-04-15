import sys

from crochet import setup as crochet_setup
crochet_setup()


def start_manhole(start_manhole, port, username, password):
    namespace = sys._getframe(2).f_locals
    start_manhole(namespace, port, username, password).wait()


def start_telnet_manhole(port=8081, username='admin', password='admin'):
    """Starting Telnet manhole

    Keyword arguments:
    port -- the telnet port (default 8081)
    username -- the user name to login (default 'admin')
    password -- the user password to login (default 'admin')

    """
    from goatpy.telnet import start as telnet_start
    start_manhole(telnet_start, port, username, password)


def start_ssh_manhole(port=8022, username='admin', password='admin'):
    """Starting SSH manhole

    Keyword arguments:
    port -- the SSH port (default 8022)
    username -- the user name to login (default 'admin')
    password -- the user password to login (default 'admin')

    """
    from goatpy.ssh import start as ssh_start
    start_manhole(ssh_start, port, username, password)
