import webapp2
import logging
import jinja2
import os


app = webapp2.WSGIApplication([
    ('/schedule', ScheduleHandler),
    ('/history', HistoryHandler)
], debug=True)
