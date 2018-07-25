import webapp2
import logging
import jinja2
import os
from google.appengine.ext import ndb
from google.appengine.api import users
<<<<<<< HEAD

=======
from google.appengine.api import urlfetch

class WaterDatabase(ndb.Model):
    name = ndb.StringProperty()
    totalWater = ndb.IntegerProperty()
    date = ndb.StringProperty()
    incWater = ndb.IntegerProperty()

class amtOfTimes:
     def __init__(name, totalWater, date, incWater):
         self.name = name
         self.totalWater = totalWater
         self.date = date
         self.incWater = incWater
>>>>>>> parent of 819b11d... Merge branch 'master' of https://github.com/seehamrun/GiterDone

class DatabaseForCoolPeople(ndb.Model):
    name = ndb.StringProperty()
    AMtOfWater = ndb.IntegerProperty()
    date = ndb.StringProperty()

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        logging.info('current user is %s' % (user.nickname()))
        template = jinja_env.get_template('templates/index.html')
        data = {
        'user_nickname': user.nickname(),
          'logoutUrl': users.create_logout_url('/')
        }
        return self.response.write(template.render(data))

class ScheduleHandler(webapp2.RequestHandler):
def get(self):
        template = jinja_env.get_template('templates/schedule.html')
<<<<<<< HEAD
        return self.response.write(template.render())
=======
        self.response.write(template.render())

        userTemp = self.request.get("temp")
        logging.info("This is user temp")
        logging.info(userTemp)

>>>>>>> parent of 819b11d... Merge branch 'master' of https://github.com/seehamrun/GiterDone

class HistoryHandler(webapp2.RequestHandler):
def get(self):
        template = jinja_env.get_template('templates/history.html')
        return self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/schedule', ScheduleHandler),
    ('/history', HistoryHandler)
], debug=True)
