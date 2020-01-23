import requests
from bs4 import BeautifulSoup

NUM = 1
URL = f"https://stackoverflow.com/jobs?q=python&sort=i&pg={NUM}"


def get_jobs():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    print(soup)
