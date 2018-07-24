from google.appengine.ext import ndb

class WaterDatabase(ndb.Model):
    name = ndb.StringProperty()
    totalWater = ndb.IntegerProperty()
    date = ndb.StringProperty()
    incWater = ndb.IntegerProperty()
