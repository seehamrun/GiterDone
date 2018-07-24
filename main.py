import webapp2
import logging
import jinja2
import os

from google.appengine.ext import ndb
from google.appengine.api import users
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

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        logging.info('current user is %s' % (user.nickname()))
        template = jinja_env.get_template('templates/home.html')
        data = {
        'user_nickname': user.nickname(),
          'logoutUrl': users.create_logout_url('/')
        }
        return self.response.write(template.render(data))


class ScheduleHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/schedule.html')
        return self.response.write(template.render())

        userTemp = self.request.get("temp")
        logging.info("This is user temp")
        logging.info(userTemp)


class HistoryHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/history.html')
        return self.response.write(template.render())


class SettingsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/settings.html')
        return self.response.write(template.render())

class AddWater(webapp2.RequestHandler):
    def post(self):
        requestUrl = self.request.get('url')
        logging.info('server saw a request to add %s to amount of water' % (requestUrl))
        waterDatabse = WaterDatabase(url=requestUrl)
        waterDatabase.put()



app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/schedule', ScheduleHandler),
    ('/history', HistoryHandler),
    ('/settings', SettingsHandler),
    ('/history', AddWater),
], debug=True)
