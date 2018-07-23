import webapp2
import logging
import jinja2
import os


app = webapp2.WSGIApplication([
    ('/add_favorite', AddFavoriteHandler),
    ('/list_favorites', ListFavoritesHandler)
], debug=True)
