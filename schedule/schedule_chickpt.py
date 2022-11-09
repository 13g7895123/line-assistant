from web_crawler.chickpt import *
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import pymysql
from config.db_mysql import *


def chickpt_breathe():
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db_config = config_db_config
    conn = pymysql.connect(**db_config)
    try:
        with conn.cursor() as cursor:
            command = "SELECT * FROM crawler_log WHERE NAME='chickpt'"
            cursor.execute(command)
            data = cursor.fetchall()
            if len(data) > 0:
                # 更新進LIST
                command = "UPDATE crawler_log SET last_process_time = '" + str(now_time) + "' WHERE name = 'chickpt'"
                cursor.execute(command)
            else:
                command = "INSERT INTO crawler_log(name, last_process_time) VALUES(%s, %s)"
                cursor.execute(command, ('chickpt', str(now_time)))
            conn.commit()
    except Exception as ex:
        print(ex)
    finally:
        conn.close()


def schedule_chickpt():
    print("process running... %s" % datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    crawler_chickpt()
    chickpt_breathe()


scheduler = BlockingScheduler(timezone="Asia/Taipei")
scheduler.add_job(schedule_chickpt, 'interval', minutes=3)
scheduler.start()
