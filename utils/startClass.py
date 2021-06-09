#!/usr/bin/env python3

import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


students_credentials = {
    'login': 'password',
}


class Click:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def login(self):
        driver = webdriver.Chrome("/Users/a.pavlov/Downloads/chromedriver")
        driver.get("https://lk.sut.ru/cabinet/#")
        users = driver.find_element_by_name('users')
        parole = driver.find_element_by_name('parole')
        users.send_keys(self.name)
        parole.send_keys(self.password)
        driver.find_element_by_name('logButton').click()

    # def start_class(self):


def click_all():

    for name, password in students_credentials.items():
        a = Click(name, password)
        a.login()


def __main__():
    click_all()


if __name__ == '__main__':
    sys.exit(__main__())