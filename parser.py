import logging
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import os
import datetime


logging.basicConfig(level=logging.INFO, filename='logfile.log')


async def request(login: str) -> str:
    async def request_url(url) -> str | None:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=int(os.getenv("TIMEOUT"))) as resp:
                    return await resp.text()
        except asyncio.TimeoutError:
            return None

    try:
        response = await request_url(f'https://{os.getenv("USERNAME")}:{os.getenv("PASSWORD")}@mon.kct.me/nagios/onu-signal.php?AbonLogin={login}')
        if response:
            soup = BeautifulSoup(response, 'lxml')
            soup.select_one('title').decompose()
            return soup.get_text()
        else:
            logging.warning(f'{datetime.datetime.now()}|Таймаут ожидания. Запрошенный логин {login}')
            return 'Неверный логин'
    except Exception as e:
        logging.error(f'{datetime.datetime.now()}|Ошибка при запросе к nagios: {e}')
        return 'Произошла ошибка'
