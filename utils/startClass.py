#!/usr/bin/env python3

import sys
from selenium import webdriver

import json
import time
import os
import base64
from selenium.webdriver.chrome.options import Options

DB_DIR = os.path.join(os.path.dirname(__file__), '..', 'resources')


class Click:
    def __init__(self, name, password):
        self.name = name
        self.password = base64.b64decode(password).decode("utf-8")

    def login(self):
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome("/Users/a.pavlov/Downloads/chromedriver", options=chrome_options)
            driver.get("https://lk.sut.ru/cabinet/#")
            driver.implicitly_wait(5)
            users = driver.find_element_by_name('users')
            parole = driver.find_element_by_name('parole')
            users.send_keys(self.name)
            parole.send_keys(self.password)
            driver.find_element_by_name('logButton').click()
            driver.find_element_by_xpath("//div//font[@title='Учеба...']//..").click()
            time.sleep(2)
            driver.find_element_by_xpath("//a[text()='Расписание']").click()
            time.sleep(2)
            driver.find_element_by_xpath("//a[text()='Начать занятие']").click()
        except Exception as exc:
            print(f'Error: {exc}')


def click_all():
    for item in os.listdir(DB_DIR):
        with open(os.path.join(DB_DIR, item), 'r') as f:
            data = json.loads(f.read())
            for name, password in data.items():
                a = Click(name, password)
                a.login()


def __main__():
    click_all()


if __name__ == '__main__':
    sys.exit(__main__())
