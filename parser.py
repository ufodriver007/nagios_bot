import logging
import requests
from bs4 import BeautifulSoup
import os


logging.basicConfig(level=logging.INFO, filename='logfile.log')


def request(login: str):
    try:
        response = requests.get(f'https://{os.getenv("USERNAME")}:{os.getenv("PASSWORD")}@mon.kct.me/nagios/onu-signal.php?AbonLogin={login}', timeout=int(os.getenv("TIMEOUT")))
        soup = BeautifulSoup(response.text, 'lxml')
        soup.select_one('title').decompose()
        return soup.get_text()
    except requests.exceptions.Timeout:
        logging.warning(f'Таймаут ожидания. Запрошенный логин {login}')
        return 'Неверный логин'
