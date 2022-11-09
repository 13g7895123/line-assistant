from line_bot_api import *
import pymysql
from config.db_mysql import *
from line_bot_push_message import *


def breathe_chickpt(event):
    db_config = config_db_config
    conn = pymysql.connect(**db_config)
    try:
        with conn.cursor() as cursor:
            command = "SELECT * FROM crawler_log WHERE NAME='chickpt'"
            cursor.execute(command)
            data = cursor.fetchall()
            if len(data) > 0:
                update_time = data[0][2]
                msg = '【小雞上工：查詢上次更新時間】\n' + str(update_time)
                push_msg(juid, msg)
    except Exception as ex:
        print(ex)
    finally:
        conn.close()
