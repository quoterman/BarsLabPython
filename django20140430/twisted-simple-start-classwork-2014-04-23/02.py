class A:
    counter = 5
    def count(self):
        from twisted.internet import reactor
        if self.counter == 0:
            reactor.stop()
        else:
            print "count: " + str(self.counter)
            reactor.callLater(1, self.count)
            self.counter -= 1

from twisted.internet import reactor
reactor.callWhenRunning(A().count)
reactor.callWhenRunning(A().count)

print "Start."
reactor.run()


