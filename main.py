import webapp2
import logging
import jinja2
import os
import time

from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import urlfetch



class WaterDatabase(ndb.Model):
    user = ndb.StringProperty()
    name = ndb.StringProperty()
    totalWater = ndb.IntegerProperty()
    age = ndb.IntegerProperty()
    height = ndb.StringProperty()
    incWater = ndb.IntegerProperty()
    weight = ndb.IntegerProperty()
    times = ndb.StringProperty(repeated=True)
    currentAmt = ndb.IntegerProperty()


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class IndexHandler(webapp2.RequestHandler):
    def get(self):
        currentUser = users.get_current_user().nickname()
        results = WaterDatabase.query(WaterDatabase.user == currentUser).fetch()
        if (len(results) > 0):
            totalWater = results[0].totalWater
            currentAmt = results[0].currentAmt
        else:
            totalWater = 0
            currentAmt = 0
        #logging.info('current user is %s' % (user.nickname()))
        template = jinja_env.get_template('templates/home.html')
        data = {
        'user_nickname': currentUser,
        'logoutUrl': users.create_logout_url('/'),
        'totalWater': totalWater,
        'currentAmt': currentAmt
        }
        return self.response.write(template.render(data))

class ScheduleHandler(webapp2.RequestHandler):
    def get(self):
        currentUser = users.get_current_user().nickname()
        results = WaterDatabase.query(WaterDatabase.user == currentUser).fetch()
        if (len(results) > 0):
            totalWater = results[0].totalWater
            amtWater = results[0].incWater
            times = results[0].times
            ounces = totalWater / amtWater
            totalSessions = results[0].currentAmt / ounces
        else:
            totalWater = 0
            amtWater = 0
            times = []
            ounces = totalWater / (amtWater + 1)
            totalSessions = 0
        # userTemp = self.request.get("temp")
        # logging.info("This is user temp")
        # logging.info(userTemp)
        list = []
        for i in range(0, amtWater):
            dict = {
            "valueText" : "value" + str(i + 1),
            "isChecked" : i < totalSessions
            }
            list.append(dict)

        template = jinja_env.get_template('templates/schedule.html')
        value = {
            "values" : list,
            "amtWater" : amtWater,
            "ounces" : ounces,
            "x" : times,
            "user_exists" : len(results)>0

        }
        logging.info(value)
        # if (userTemp>80) :
        #     logging.info("its hot")
        #     print("It is hot.")
        return self.response.write(template.render(value))

    def post(self):
        #logging.info(self.request.get("value2"))
        currentUser = users.get_current_user().nickname()
        results = WaterDatabase.query(WaterDatabase.user == currentUser).fetch()
        if (len(results) > 0):
            totalWater = results[0].totalWater
            amtWater = results[0].incWater
            ounces = totalWater / amtWater
        else:
            totalWater = 0
            amtWater = 0
            ounces = totalWater / (amtWater + 1)

        currentAmt = 0
        logging.info(self.request.POST)
        for i in range(1, amtWater + 1):
            if(int(self.request.get("value" + str(i), 0)) == ounces):
                currentAmt = currentAmt + ounces
        logging.info(currentAmt)
        results[0].currentAmt = currentAmt
        results[0].put()
        #newentry = WaterDatabase(currentAmt = currentAmt)
        #newentry.put()
        time.sleep(1)
        self.redirect('/history')





class HistoryHandler(webapp2.RequestHandler):
    def get(self):
        results = WaterDatabase.query().fetch()
        if (len(results) > 0):
            totalWater = results[0].totalWater
            amtWater = results[0].incWater
            ounces = totalWater / amtWater
            currentAmt = results[0].currentAmt
        else:
            totalWater = 0
            amtWater = 0
            ounces = totalWater / (amtWater + 1)
            currentAmt = 0
        checks = self.request.get('checks')
        template = jinja_env.get_template('templates/history.html')
        value = {
            "totalWater" : totalWater,
            "currentAmt" : currentAmt
        }
        return self.response.write(template.render(value))



class AboutUsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/aboutus.html')
        return self.response.write(template.render())


class SettingsHandler(webapp2.RequestHandler):
    def get(self):
        currentUser = users.get_current_user().nickname()
        results = WaterDatabase.query(WaterDatabase.user == currentUser).fetch()
        if len(results) == 0:
            data = {
            "userName": "",
            "userAge": "",
            "userHeight": "",
            "userWeight": "",
            "userWaterGoal": "",
            "numberReminderTimes": "",
            "reminderTime1": "",
            "reminderTime2": "",
            "reminderTime3": "",
            "reminderTime4": "",
            "reminderTime5": "",
            "reminderTime6": "",
            "reminderTime7": "",
            "reminderTime8": "",
            "reminderTime9": "",
            "reminderTime10": "",
            "reminderTime11": "",
            "reminderTime12": "",

            }
        else:
            data = {
            "userName": results[0].user,
            "userAge": results[0].age,
            "userHeight": results[0].height,
            "userWeight": results[0].weight,
            "userWaterGoal": results[0].totalWater,
            "numberReminderTimes":results[0].incWater,
            }
            for i in range(12):
                if len(results[0].times)>i:
                    data["reminderTime" + str(i + 1)] = results[0].times[i]

        template = jinja_env.get_template('templates/settings.html')

        return self.response.write(template.render(data))

    def post(self):
        currentUser = users.get_current_user().nickname()
        #  1. get all the things from self.request.get()
        name = self.request.get('name')
        age = int(self.request.get('age'))
        height = self.request.get('height')
        weight = int(self.request.get('weight'))
        totalWater = int(self.request.get('totalWater'))
        incWater = int(self.request.get('incWater'))
        times = []
        self.response.headers['Content-Type'] = 'text/html'
        for i in range(incWater):
            times.append(self.request.get("reminderTime" + str(i+1)))
        # make a new WaterDatabase using the things from 1
        newentry = WaterDatabase(user = currentUser, name=name, age=int(age), height=height, weight=weight, totalWater=totalWater, incWater=incWater, times = times, currentAmt= 0)

        # put that info in the db
        newentry.put()
        time.sleep(1)
        self.redirect('/schedule')



class AddWater(webapp2.RequestHandler):
    def post(self):
        requestUrl = self.request.get('url')
        logging.info('server saw a request to add %s to amount of water' % (requestUrl))
        waterDatabase = WaterDatabase(url=requestUrl)
        waterDatabase.put()


app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/schedule', ScheduleHandler),
    ('/history', HistoryHandler),
    ('/settings', SettingsHandler),
    ('/aboutus', AboutUsHandler)
], debug=True)
