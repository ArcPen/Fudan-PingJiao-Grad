from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from random import random

usrname = ''
password = ''
sleep_time = 10 # select how many seconds to wait in finishing each task 

driver = webdriver.Chrome()
url = "https://yzsfwapp.fudan.edu.cn/gsapp/sys/wspjappfudan/*default/index.do"

driver.get(url)
usr = driver.find_element(By.ID, 'username')
pwd = driver.find_element(By.ID, 'password')
submit = driver.find_element(By.ID, 'idcheckloginbtn')

usr.send_keys(usrname)   #填入uis用户名
pwd.send_keys(password)   #填入uis密码
submit.click()

time.sleep(3)
# if there's shut, shut it.
try:
    driver.find_element(By.ID, 'guideShut').click()
    # shut.click()
except Exception as e: # better change it to NotFoundException
    pass

while True:
    driver.get(url)
    time.sleep(2)
    try:
        driver.find_element(By.ID, 'guideShut').click()
    except Exception as e: # better change it to NotFoundException
        pass

    xpath = '/html/body/main/article/section/div[2]/div/div[2]/div/div/div/div/div/div'
    task_list = driver.find_elements(By.XPATH, xpath)
    task_completed = ['success' in i.find_element(By.XPATH, './div').get_attribute('class') for i in task_list]
    # print("Total tasks:", len(task_list), "Finished tasks:", sum(task_completed))
    print(f"Tasks to go: {len(task_list)-sum(task_completed)}, Total tasks: {len(task_list)}")
    if sum(task_completed) == len(task_list):
        print("All tasks finished! Exiting...")
        break
    for i in range(len(task_list)): # Go to the first unfinished task.
        if not task_completed[i]:
            print(task_list[i].find_element(By.XPATH, './div/div[2]').get_attribute('title'))
            task_list[i].click()
            break

    # if there's shut, shut it.
    time.sleep(3)
    try:
        driver.find_element(By.ID, 'guideShut').click()
    except Exception as e: # better change it to NotFoundException
        pass

    
    # find all the radio buttons
    xpath = '/html/body/div[14]/div/div[1]/section/div/div[*]/div'
    radio_list = driver.find_elements(By.CLASS_NAME, 'paper_tm')
    print("Total radio buttons: ", len(radio_list))
    for i in range(len(radio_list)):
        grad = 1 if random() < 0.9 else 2 # 0.9 chance of choosing the first one
        node = radio_list[i].find_element(By.XPATH, f'./div/label[{grad}]')
        # print(node.find_element(By.XPATH, './span').text)
        driver.execute_script("arguments[0].click();", node)
        driver.implicitly_wait(1)
    
    # confirm and submit
    time.sleep(sleep_time)
    driver.find_element(By.XPATH, '//a[text()="提交"]').click()
    driver.find_element(By.XPATH, '//a[text()="确定"]').click()
