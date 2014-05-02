from twisted.internet import reactor, task
from time import ctime

def t():
    print ctime()

def u():
    print "Shuhrat"

task01 = task.LoopingCall(t)
task01.start(1.0)

task02 = task.LoopingCall(u)
task02.start(3)

reactor.run()

