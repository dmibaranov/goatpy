from twisted.conch.insults import insults
from twisted.conch import manhole, manhole_ssh
from twisted.cred.checkers import (
    InMemoryUsernamePasswordDatabaseDontUse as MemoryDB)
from twisted.cred.portal import Portal
from crochet import in_reactor


@in_reactor
def start(reactor, namespace, port, username, password):
    sshRealm = manhole_ssh.TerminalRealm()

    def chainedProtocolFactory():
        return insults.ServerProtocol(manhole.Manhole, namespace)
    sshRealm.chainedProtocolFactory = chainedProtocolFactory

    portal = Portal(sshRealm, [MemoryDB(**{username: password})])
    reactor.listenTCP(port, manhole_ssh.ConchFactory(portal))
