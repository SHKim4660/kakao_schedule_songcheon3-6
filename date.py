from pytz import timezone
from datetime import datetime
import time, win32con, win32api, win32gui
import requests
import bs4
import schedule
from datetime import timedelta


now = datetime.now(timezone('Asia/Seoul'))

day_of_week = now.weekday() #Date Of Week 현재 요일
year = now.year
month = now.month
day = now.day
hour = now.hour
min = now.minute

nextday = now + timedelta(days=1)

print(nextday.strftime("%d"))
