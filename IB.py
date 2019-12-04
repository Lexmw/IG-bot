from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def closeBrowser(self):
        self.driver.close()


    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        username_input = driver.find_element_by_xpath("//input[@name='username']")
        username_input.clear()
        username_input.send_keys(self.username)
        password_input = driver.find_element_by_xpath("//input[@name='password']")
        password_input.clear
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.RETURN)

    #This takes care of the notifictions question that appears on ig
    def no_Notifications(self):
        time.sleep(2)
        driver = self.driver
        Not_Now_button = driver.find_element_by_xpath("//button[text()='Not Now']")
        Not_Now_button.click()
        time.sleep(2)


    def likephoto(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/") 
        time.sleep(2)

        #getting the photos
        pic_hrefs = []
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            #getting the anchor tags
            hrefs = driver.find_elements_by_tag_name('a')

            #creating an array of photos
            pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
            [pic_hrefs.append(href) for href in hrefs if href not in pic_hrefs]
            print(hashtag + 'photos:'+ str(len(pic_hrefs)))

        #liking the photos
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(2)
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            try:
                driver.find_element_by_xpath("//span[@aria-label='Like']").click()
                time.sleep(20)
            except:
                time.sleep(2) 

LexIG = InstagramBot("ladaayylexx", "Greatness22")
LexIG.login()
LexIG.no_Notifications()
LexIG.likephoto('sustainability')
print('this runs')