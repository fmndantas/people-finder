import autoit
from autoit.autoit import properties
from time import sleep
import os

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys


def send_text_data(driver, phone, msg):
    driver.get('https://web.whatsapp.com/send?phone={}'.format(phone))
    try:
        # Verify valid number. If the number doesn't exist, raise TimeoutException
        WebDriverWait(driver, 5).until_not(EC.presence_of_element_located(('class name', '_2dA13')))
    except TimeoutException:
        return None
    try:
        # Verify if the text box has appeared in the screen. If not, raise TimeoutException
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(('class name', '_2S1VP')))
    except TimeoutException:
        return None
    textbox = driver.find_element_by_class_name('_2S1VP')
    textbox.send_keys(msg)
    sleep(5)
    return msg


def send_image_data(driver, phone, img_path, img_label):
    # From here, assumes that the user is logged in
    if os.path.exists(img_path):
        driver.get('https://web.whatsapp.com/send?phone={}'.format(phone))
        while True:  # Fast version
            try:
                assert (len(driver.find_elements_by_xpath('//header')) == 2)
            except AssertionError:
                continue
            else:
                break
        while True:
            try:
                driver.find_elements_by_xpath('//div[@title="Attach"]')[0].click()
            except Exception as Error:
                continue
            else:
                break
        image = driver.find_elements_by_xpath('//button[@data-animate-menu-icons-item="true"]')[0]
        image.click()
        autoit.win_wait("File Upload")
        # Minimize
        autoit.win_set_state("File Upload", properties.SW_MINIMIZE)
        sleep(2)
        autoit.control_send("File Upload", "[CLASS:Edit]", img_path, mode=0)
        sleep(2)
        autoit.control_click("File Upload", "[CLASS:Button]")
        autoit.win_close("File Upload")
        autoit.win_wait_close("File Upload")
        sleep(2)
        img_label_box = driver.find_elements_by_xpath('//div[@spellcheck="true"]')[0]
        if img_label:
            img_label_box.send_keys(img_label)
        img_label_box.send_keys(Keys.ENTER)
        sleep(2)
        return img_label
    else:
        # The file is wrong
        return None


