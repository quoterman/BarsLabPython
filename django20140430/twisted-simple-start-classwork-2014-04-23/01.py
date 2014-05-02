def hi():
    print "Hello!"
    from twisted.internet import reactor
    reactor.stop()

from twisted.internet import reactor

reactor.callWhenRunning(hi)

print "Starting reactor"
reactor.run()


#reactor.callLater(n, f)