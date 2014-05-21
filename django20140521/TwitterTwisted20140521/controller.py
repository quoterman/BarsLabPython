from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.web.template import Element, XMLFile, tags, flattenString, renderer
from twisted.python.filepath import FilePath
import sqlite3

conn = sqlite3.connect("db.db")
c = conn.cursor()

class IndexElement(Element):
    loader = XMLFile(FilePath("index.xml"))

    @renderer
    def header(self, request, tag):
        return tag(tags.p(tags.b("Header")), id="header")

    @renderer
    def real_twitter(self, request, tag):
        tag.fillSlots(real_twitter_url="http://twitter.com")
        return tag


    @renderer
    def tweet_list(self, request, tag):
        tweets = c.execute("select * from tweets")
        for tweet in tweets:
            yield tag.clone().fillSlots(tweet=tweet)


class TwitterResource(Resource):

    def render_GET(self, request):
        return flattenString(request, IndexElement()).result

    def render_POST(self, request):
        tweet = request.args["tweet"][0]
        c.execute("insert into tweets values(?)",(tweet,))
        conn.commit()
        print request.args

        return flattenString(request, IndexElement()).result

    def getChild(self, path, request):
        return self

t = TwitterResource()

s = Site(t)
reactor.listenTCP(1234,s)
reactor.run()