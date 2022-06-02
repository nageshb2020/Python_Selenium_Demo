import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import sys

def testfirstDemo():
    chrome_driver = webdriver.Chrome("D:\Driver\chromedriver.exe")

    chrome_driver.get("http://google.com")
    sleep(10)

def firstDemotest():
    chrome_driver = webdriver.Chrome("D:\Driver\chromedriver.exe")

    chrome_driver.get("http://google.com")
    sleep(10)