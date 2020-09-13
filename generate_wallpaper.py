import configparser
from unsplash.api import Api
from unsplash.auth import Auth

config = configparser.ConfigParser()
config.read('config.ini')

client_id = config['API Credentials']['client_id']
client_secret = config['API Credentials']['client_secret']
redirect_uri = config['API Credentials']['redirect_uri']

auth = Auth(client_id, client_secret, redirect_uri)
api = Api(auth)