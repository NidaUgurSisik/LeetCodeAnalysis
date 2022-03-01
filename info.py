headlessMode=False 
delay= 4 #sn

from re import T, X, search
from sys import displayhook
import FileIO
import urllib

from dateutil import rrule
from datetime import date


import urllib
import selenium
from selenium_stealth import stealth
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
import logging
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
from datetime import timedelta
import os
from selenium.webdriver.support.ui import Select
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import captchaSolver
from selenium.common.exceptions import ElementNotVisibleException, TimeoutException
from selenium.common.exceptions import NoSuchElementException
from itertools import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

logging.basicConfig(level = logging.INFO)



class Bot:
    driver=None
    START_URL="https://leetcode.com/problemset/all/"

    def __init__(self):
        logging.info("bot is starting")

        #WEBDRIVER CONFIG
        options = Options()
        options.add_argument("--log-level=3")
        options.add_argument("--user-data-dir=c:\\temp\\profifgle4205")
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation","test-type"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument('--disable-gpu')
        options.add_argument("--log-level=3")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/536.36 (KHTML, like Gecko) Chrome/95.0.4664.110 Safari/537.36")
        options.headless = headlessMode
        options.page_load_strategy = 'eager'
        self.driver= webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
        self.driver.execute_cdp_cmd("Network.enable", {})
        self.driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4663.110 Safari/537.36"}})
   
    def isElementExists(self,xpath):
        try:
            elem= self.driver.find_element(By.XPATH,xpath)
            return True
        except NoSuchElementException as E:
            return False

    def clickElement(self,xpath):
        try:
            self.waitForElementToAppear(xpath,5)
            element=self.driver.find_element(By.XPATH, xpath)
            self.driver.execute_script("arguments[0].click();",element)
        except:
            raise 

    def waitForElementToAppear(self,xpath,timeout=3):
        try:
            element_present = EC.presence_of_element_located((By.XPATH, xpath))
            WebDriverWait(self.driver, timeout).until(element_present)  
        except ElementNotVisibleException:
            return False
            raise     


    def starting(self):
        self.driver.get("https://leetcode.com/problemset/all/")



    def run(self):
        self.starting()
        for i in range(2,45,1):
            for leetcode in self.driver.find_elements_by_css_selector('div[class="odd:bg-overlay-3 dark:odd:bg-dark-overlay-1 even:bg-overlay-1 dark:even:bg-dark-overlay-3"]'):
                Name = leetcode.find_element_by_css_selector('div[role="cell"]:nth-child(2)').text
                Percentage = leetcode.find_element_by_css_selector('div[role="cell"]:nth-child(4)').text
                difficulty = leetcode.find_element_by_css_selector('div[role="cell"]:nth-child(5)').text

                #time.sleep(1)
                strr = Name + " , " + Percentage.replace("%","") +" , "+ difficulty
            
                FileIO.dosyayaYaz("FinalLeetcode.csv", strr + "\n")

            self.driver.get("https://leetcode.com/problemset/all/?page=" + str(i))

#DEBUG:
api= Bot()
api.run()
