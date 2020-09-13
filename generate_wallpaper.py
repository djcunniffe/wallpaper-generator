import configparser
import requests
import ctypes
import os
from unsplash.api import Api
from unsplash.auth import Auth

config = configparser.ConfigParser()
config.read('config.ini')

client_id = config['API Credentials']['client_id']
client_secret = config['API Credentials']['client_secret']
redirect_uri = config['API Credentials']['redirect_uri']

auth = Auth(client_id, client_secret, redirect_uri)
api = Api(auth)


orientation = config['Photo Config']['orientation']
query = config['Photo Config']['query']
featured = config['Photo Config']['featured']
random_photo = api.photo.random(query=query, orientation=orientation, featured=featured)[0]


def get_download_link(Photo):
    return Photo.links.download
    
def download_photo(download_link, filename='background.jpg'):
    f = open(filename, 'wb')
    f.write(requests.get(download_link).content)
    return filename

def set_desktop_background(filename):
    real_path = os.path.realpath(filename)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, real_path , 0)

download_link = get_download_link(random_photo)
set_desktop_background(download_photo(download_link))