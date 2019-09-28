import requests
from bs4 import BeautifulSoup

class ChromedriverLib(object):

  def __init__(self):
    res = requests.get("https://chromedriver.storage.googleapis.com/?delimiter=/&prefix=")
    soup = BeautifulSoup(res.content, features="html.parser")
    prefixes = soup.find_all("prefix")
    prefixes = [prefix.text[:-1] for prefix in prefixes if prefix.text and prefix.text != 'icons/']
    self.versions = sorted(prefixes)

  def get_latest_version(self):
    return self.versions[-1]
