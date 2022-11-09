from line_bot_api import *
import pymysql
from config.db_mysql import *


def get_data():
    db_config = config_db_config
    conn = pymysql.connect(**db_config)
    try:
        with conn.cursor() as cursor:
            command = "SELECT * FROM crawler_log WHERE NAME='chickpt'"
            cursor.execute(command)
            data = cursor.fetchall()
            if len(data) > 0:
                update_time = data[0][2]
                return update_time
    except Exception as ex:
        print(ex)
    finally:
        conn.close()


def breathe_chickpt(event):
    update_time = get_data()
    msg = '【小雞上工：查詢上次更新時間】\n' + str(update_time)
    # msg = 'testt'
    text_message = TextSendMessage(msg)
    line_bot_api.reply_message(event.reply_token, text_message)
