from crochet import in_reactor


@in_reactor
def start_repl(reactor, port=8081, namespace={}):
    from twisted.manhole.telnet import ShellFactory
    shell_factory = ShellFactory()
    shell_factory.namespace = namespace
    reactor.listenTCP(port, shell_factory)
