from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

hashtag_list = ['games', 'mobilegames']
profile_hrefs = []
pic_hrefs = []
prev_user_list = []
new_followed = []
followed = 0
likes = 0
comments = 0



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
        login_button = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
        login_button.click()
        time.sleep(2)
        username_input = driver.find_element_by_xpath(
            "//input[@name='username']")
        username_input.clear()
        username_input.send_keys(self.username)
        password_input = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_input.clear
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.RETURN)

    #This takes care of the notifictions question that appears on ig
    def no_Notifications(self):
        time.sleep(2)
        driver = self.driver
        Not_Now_button = driver.find_element_by_xpath(
            "/html/body/div[4]/div/div/div[3]/button[2]")
        Not_Now_button.click()
        time.sleep(2)

    def likephoto(self, hashtag_list):
        tag = -1
        for hashtag in hashtag_list:
            tag += 1
            driver = self.driver
            driver.get("https://www.instagram.com/explore/tags/" +
                       hashtag_list[tag] + "/")
            print('this is the hashtag I just looked up', hashtag_list[tag])
            time.sleep(2)

            #getting the photos
            for i in range(1, 2):
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)

                #getting the anchor tags
                hrefs = driver.find_elements_by_tag_name('a')

                #creating an array of photos
                pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
                # [pic_hrefs.append(href)]
                #  for href in hrefs if href not in pic_hrefs]
                print('photos from :', hashtag, str(len(pic_hrefs)))
                time.sleep(2)

                followed = 0
                likes = 0
            for pic_href in pic_hrefs:
                driver.get(pic_href)
                time.sleep(10)
                driver.execute_script(
                    "window.scrollTo(0,document.body.scrollHeight);")
                try:
                    driver.find_element_by_xpath("//span[@aria-label='Like']").click()
                    likes += 1

                    username = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/header/div[2]/div[1]/div[1]/h2/a').text
                    print(username)

                    if username not in prev_user_list:
                    
                    if driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':

                        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/header/div[2]/div[1]/div[2]/button').click()
                        new_followed.append(username)
                        followed += 1
                    time.sleep(20)
                except:
                    time.sleep(10)

LexIG = InstagramBot("username", "password")
LexIG.login()
LexIG.no_Notifications()
LexIG.likephoto(hashtag_list)
LexIG.toFollow(hashtag_list)
print('Liked {} photos.'.format(likes))
print('Followed {} new people.'.format(followed))