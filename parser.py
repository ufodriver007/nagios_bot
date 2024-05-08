import requests
from bs4 import BeautifulSoup
import os


def request(login: str):
    try:
        response = requests.get(f'https://{os.getenv("USERNAME")}:{os.getenv("PASSWORD")}@mon.kct.me/nagios/onu-signal.php?AbonLogin={login}', timeout=3)
        soup = BeautifulSoup(response.text, 'lxml')
        soup.select_one('title').decompose()
        return soup.get_text()
    except requests.exceptions.Timeout:
        return 'Неверный логин'
