from web_crawler.chickpt import *
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


def schedule_chickpt():
    print("process running... %s" % datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    crawler_chickpt()


scheduler = BlockingScheduler(timezone="Asia/Taipei")
scheduler.add_job(schedule_chickpt, 'interval', minutes=3)
scheduler.start()
