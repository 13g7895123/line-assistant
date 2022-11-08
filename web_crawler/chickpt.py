from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from web_address import *
from line_bot_api import *


def crawler_chickpt(event):
    # 制定關鍵字
    key_word_list = ['PHP', 'php', 'sql', 'SQL', 'Python', 'PYTHON',
                     'python', 'web', 'Web', 'WEB', '網頁', '網站', '爬蟲']

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-popup-blocking')

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get(chickpt)

    # 找到目標段落
    ul = driver.find_element(By.XPATH, "//ul[@id='job-list']")
    lis = ul.find_elements(By.XPATH, "li")

    for li in lis:
        # 取得標題
        title = li.find_element(By.XPATH, "a/div[@class='is-blk']/h2").text
        # 判斷是否有關鍵字
        for key_word in key_word_list:
            if key_word in title:
                money = li.find_element(By.XPATH,
                                        "a/div[@class='is-blk']/p[@class='job_detail']/span[@class='salary']").text
                location = li.find_element(By.XPATH,
                                           "a/div[@class='is-blk']/p[@class='job_detail']/span[@class='place']").text
                link = li.find_element(By.XPATH, "a").get_attribute('href')
                msg = 'TITLE: ' + title + '\n MONEY: ' + money + '\n LOCATION: ' + location + '\n' + link
                text_message = TextSendMessage(link)
                line_bot_api.reply_message(event.reply_token, text_message)


crawler_chickpt('1')

