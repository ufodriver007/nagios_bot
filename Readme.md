## Развёртывание бота
1. Клонируем репозиторий и переходим в его директорию
```angular2html
git clone https://github.com/ufodriver007/nagios_bot.git
```
2. Создаём файл с переменными окружения `.env` Заполняем этот файл по примеру файла `.env.example`
3. Создаём виртуальное окружение Python. Версия Python >= 3.11
```angular2html
python3.11 -m venv venv
```
4. Активируем виртуальное окружение из свежесозданной директории `venv`
```angular2html
source venv/bin/activate
```

5. Устанавливаем зависимости в виртуальное окружение
```angular2html
pip install -r requirements.txt
```
Деактивировать виртуальное окружение можно с помощью команды `deactivate`

6. Создание юнита в Systemd и запуск демона
```angular2html
cd /etc/systemd/system/
```
```angular2html
sudo nano nagios_bot.service
```
Пример сервиса
```angular2html
[Unit]
Description=nagios_bot
After=syslog.target
After=network.target

[Service]
Type=simple
User=mike
WorkingDirectory=/home/mike/nagios_bot
ExecStart=/home/mike/nagios_bot/venv/bin/python3 /home/mike/nagios_bot/bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```
Перезапуск службы
```angular2html
sudo systemctl daemon-reload
```
запускаем только что созданный юнит
```angular2html
sudo systemctl enable nagios_bot
sudo systemctl start nagios_bot
```

#### Соответственно остановка/перезапуск бота происходит так
```angular2html
sudo systemctl stop nagios_bot
```
```angular2html
sudo systemctl restart nagios_bot
```
