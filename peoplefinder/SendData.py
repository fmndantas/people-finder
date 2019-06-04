import autoit
from autoit.autoit import properties
from time import sleep
import os
import pdb

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.keys import Keys

def send_text_data(driver, phone, msg):
    driver.get('https://web.whatsapp.com/send?phone={}'.format(phone))
    text_box_xpath = "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]"
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, text_box_xpath)))
    except TimeoutException:
        return None
    text_box = driver.find_element(By.XPATH, text_box_xpath)
    text_box.send_keys(msg)
    text_box.send_keys(Keys.ENTER)
    sleep(1)

def send_image_data(driver, phone, img_path, img_label):
    # From here, assumes that the user is logged in
    if os.path.exists(img_path):
        driver.get('https://web.whatsapp.com/send?phone={}'.format(phone))
        clip_xpath = '/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]'
        image_xpath = '/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button'
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, clip_xpath)))
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/div/div[2]/h1')
        except TimeoutException:
            return None
        except NoSuchElementException:
            pass
        driver.find_element(By.XPATH, clip_xpath).click()
        driver.find_element(By.XPATH, image_xpath).click()
        autoit.win_wait("File Upload")
        pdb.set_trace()
        # Minimize
        autoit.win_set_state("File Upload", properties.SW_MINIMIZE)
        pdb.set_trace()
        autoit.control_send("File Upload", "[CLASS:Edit]", img_path, mode=0)
        # todo pyautoit typing incorrect image address here
        pdb.set_trace()
        sleep(1)
        autoit.control_click("File Upload", "[CLASS:Button]")
        pdb.set_trace()
        autoit.win_close("File Upload")
        pdb.set_trace()
        autoit.win_wait_close("File Upload")
        pdb.set_trace()
        add_caption_xpath = '/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/span/div/div[2]/div/div[3]/div[1]'
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, add_caption_xpath)))
        except (TimeoutError, NoSuchElementException):
            return None
        pdb.set_trace()
        add_caption = driver.find_element(By.XPATH, add_caption_xpath)
        pdb.set_trace()
        if img_label:
            add_caption.send_keys(img_label)
        add_caption.send_keys(Keys.ENTER)
        sleep(2)  # waits until the image has been sent
        return img_label
    else:
        # The file is wrong
        driver.close()