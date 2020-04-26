import time
from .scrapper import getUpcomingTask, getLoginInfo, getCourseList
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options

login_page =  'https://v-class.gunadarma.ac.id/login'
upcoming_page = 'https://v-class.gunadarma.ac.id/calendar/view.php?view=upcoming'
dashboard_page = 'https://v-class.gunadarma.ac.id/my/'
course_page = 'https://v-class.gunadarma.ac.id/course/view.php?id='#+course_id

# MainApp
class VCheck():
    def __init__(self):
        self.wait_time = 5

        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)
        self.auth = False

    def login(self, uname, pwd):
        self.driver.get(login_page)
        self.driver.find_element_by_id('username').send_keys(uname)
        self.driver.find_element_by_id('password').send_keys(pwd)
        self.driver.find_element_by_id('loginbtn').click()
        time.sleep(self.wait_time)

        self.auth = getLoginInfo(self.driver.page_source)

    def getUpcomingTask(self):
        if self.auth:
            self.driver.get(upcoming_page)
            time.sleep(self.wait_time)

            return getUpcomingTask(self.driver.page_source)

    def getCourseList(self):
        if self.auth:
            self.driver.get(dashboard_page)
            time.sleep(self.wait_time)

            return getCourseList(self.driver.page_source)

    def setWaitTime(self, time):
        self.wait_time = time

    def endConnection(self):
        self.driver.quit()