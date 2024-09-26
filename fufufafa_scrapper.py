from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
import csv

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


def fufufafa_scrapper(driver, page=1):
    article_list = []
    article_title = []
    article_owner = []
    article_date = []
    fu_reply = []
    for i in range(page):
        url = f"https://www.kaskus.co.id/@fufufafa/viewallposts/{i+1}/?sort=desc"
        print(url)
        driver.get(url)
        driver.implicitly_wait(10)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")

        article_list = soup.find_all(class_="Mb(8px) Bd(borderSolidLightGrey)")
        for article in article_list:
            try:
                article_title.append(article.find(
                    class_="Fw(500) C(c-primary) Fz(18px) Mb(8px)").text)
            except:
                article_title.append("No Title")

            try:
                article_owner.append(article.find(
                    class_="C(c-secondary) Fw(500)").text)
            except:
                article_owner.append("No Owner")
            try:
                article_date.append(article.find(
                    class_="Fz(12px) C(c-secondary)").text)
            except:
                article_date.append("No Date")
            try:
                fu_reply.append(article.find(
                    class_="C(c-secondary) Lh(1.5)").text)
            except:
                fu_reply.append("No FU Reply")

    driver.quit()
    return article_title, article_owner, article_date, fu_reply


def check(article_title, article_owner, article_date, fu_reply):
    for i in range(len(article_title)):
        print(f"Date        : {article_date[i]}")
        print(f"Owner       : {article_owner[i]}")
        print(f"Title       : {article_title[i]}")
        print(f"FU Reply    : {fu_reply[i]}")
        print()


def save_to_csv(article_title, article_owner, article_date, fu_reply):
    with open('fufufafa.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Owner", "Title", "FU Reply"])
        # convert date to datetime
        for i in range(len(article_title)):
            writer.writerow([article_date[i], article_owner[i],
                            article_title[i], fu_reply[i]])


article_title, article_owner, article_date, fu_reply = fufufafa_scrapper(
    driver, 50)
save_to_csv(article_title, article_owner, article_date, fu_reply)
