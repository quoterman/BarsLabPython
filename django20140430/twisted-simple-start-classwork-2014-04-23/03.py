def f():
    print "something is gonna happen"
    raise ArithmeticError

def g():
    print "I'm here"
    for i in range(100):
        print i

from twisted.internet import reactor

reactor.callWhenRunning(f)
reactor.callWhenRunning(g)

reactor.run()