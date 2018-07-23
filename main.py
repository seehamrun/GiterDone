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

class HistoryHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/history.html')
        return self.response.write(template.render())


class SettingsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/settings.html')
        return self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/schedule', ScheduleHandler),
    ('/history', HistoryHandler),
    ('/settings', SettingsHandler),
], debug=True)
