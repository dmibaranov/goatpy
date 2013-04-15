from crochet import in_reactor
from twisted.manhole.telnet import ShellFactory


@in_reactor
def start(reactor, namespace, port, username, password):
    shell_factory = ShellFactory()
    shell_factory.username = username
    shell_factory.password = password
    shell_factory.namespace = namespace
    reactor.listenTCP(port, shell_factory)
