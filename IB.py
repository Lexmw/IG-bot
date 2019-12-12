from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

hashtag_list = ['games']
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
            "//a[@href='/accounts/login/?source=auth_switcher']")
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
            "//button[text()='Not Now']")
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
                [pic_hrefs.append(href)
                
                #  for href in hrefs if href not in pic_hrefs]
                print(hashtag + 'photos:' + str(len(pic_hrefs)))

            #follow the 
            #     followed = 0
            #     likes = 0
            # for pic_href in pic_hrefs:
            #     driver.get(pic_href)
            #     time.sleep(10)
            #     driver.execute_script(
            #         "window.scrollTo(0,document.body.scrollHeight);")
            #     try:
            #         driver.find_element_by_xpath("//span[@aria-label='Like']").click()
            #         likes += 1

            #         username = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/header/div[2]/div[1]/div[1]/h2/a').text
            #         print(username)
                    
            #         if driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':

            #             driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/header/div[2]/div[1]/div[2]/button').click()
            #             new_followed.append(username)
            #             followed += 1
            #         time.sleep(20)
            #     except:
            #         time.sleep(10)


    # to make the follow function work on its own, it still needs to be able the profiles themsleves not jsut from the photos
    # so that it doesnt need to store post urls it needs to store profile urls
    # once that works it can run as its own script and not a part of the existing like script, unless we want it to do that.


    # I dont know whats more valuable, to be able to follow and like in the same script or to have the scripts in two different places
    # that means that they will have to run one after the other instead of working together

    #it might honestly be easier to run them in the same time because they can work together and it wont have to go through and work so hard

    # would it be valuable to make a bot that will send DMs? How will this work? will it be concurrent? Will it work one at a time?
    def toFollow(self,hashtag_list):
        
        followed = 0
        driver = self.driver

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

                #creating an array of profiles
                profile_hrefs = [elem.get_attribute('href') for elem in hrefs]
                [profile_hrefs.append(href)
                #  for href in hrefs if href not in profile_hrefs]
                print(hashtag + 'photos:' + str(len(pic_hrefs)))

        for profile_href in profile_hrefs:
            driver.get(pic_href)
            time.sleep(3)

            for x in range(1, 20):
                username = driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/div/div/article/header/div[2]/div[1]/div[1]/h2/a').text
                print(username)

                if username not in prev_user_list:
                    #if we already follow, do not unfollow
                    if driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':

                        driver.find_element_by_xpath(
                            '//*[@id="react-root"]/section/main/div/div/article/header/div[2]/div[1]/div[2]/button').click()

                        new_followed.append(username)
                        followed += 1

                    else:
                        driver.find_elements_by_link_text('Next').click()
                        time.sleep(20)

        for n in range(0,len(new_followed)):
            prev_user_list.append(new_followed[n])



LexIG = InstagramBot("ladaayylexx", "Greatness22")
LexIG.login()
LexIG.no_Notifications()
LexIG.toFollow(hashtag_list)
LexIG.likephoto(hashtag_list)
print('Liked {} photos.'.format(likes))
print('Followed {} new people.'.format(followed))
