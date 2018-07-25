import webapp2
import logging
import jinja2
import os
<<<<<<< HEAD
=======
import database

>>>>>>> parent of 991a8ea... h
from google.appengine.ext import ndb
from google.appengine.api import users
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

class HistoryHandler(webapp2.RequestHandler):
def get(self):
        template = jinja_env.get_template('templates/history.html')
        return self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/schedule', ScheduleHandler),
    ('/history', HistoryHandler)
], debug=True)
