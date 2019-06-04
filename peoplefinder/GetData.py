import os
from time import sleep

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException

def text(driver):
    """Returns contact status"""
    header_xpath = '/html/body/div[1]/div/div/div[4]/div/header'
    while True:
        try:
            driver.find_element(By.XPATH, header_xpath).click()
        except ElementClickInterceptedException:
            continue
        else:
            break
    sleep(1)
    # abt_n_phn_nmbr_xpth = '/html/body/div[1]/div/div/div[2]/div[3]/span/div/span/div/div/div/div[4]/div[1]/span'
    # try:
    #     WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, abt_n_phn_nmbr_xpth)))
    # except NoSuchElementException:
    #     return None
    status_xpath = '/html/body/div[1]/div/div/div[2]/div[3]/span/div/span/div/div/div/div[4]/div[2]/div/div'
    number_xpath = '/html/body/div[1]/div/div/div[2]/div[3]/span/div/span/div/div/div/div[4]/div[3]/div/div'
    try:
        driver.find_element(By.XPATH, number_xpath)
    except NoSuchElementException:
        return None  # No status
    else:
        return driver.find_element(By.XPATH, status_xpath).text  # There's status


def screenshot(driver, savedir, phone):
    """Performs a screenshot in number profile if it has photo and returns the name of the resulting file"""
    filename = os.path.join(savedir, phone + '.png')
    picbox_xpath = '/html/body/div[1]/div/div/div[2]/div[3]/span/div/span/div/div/div/div[1]/div[1]/div/img'
    pic_xpath = '/html/body/div[1]/div/span[3]/div/div/div[2]/div/div/div/div/img'
    try:
        driver.find_element(By.XPATH, picbox_xpath).click()
    except (NoSuchElementException, ElementNotInteractableException):  # No profile pic
        return None
    else:
        sleep(2)
        driver.find_element(By.XPATH, pic_xpath).screenshot(filename)  # There's profile pic
        return filename


def get_data(driver, phone, savedir):
    """Takes the photo and number of a given contact in WhatsApp"""
    driver.get('https://web.whatsapp.com/send?phone={}'.format(phone))
    header_xpath = '/html/body/div[1]/div/div/div[4]/div/header'
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, header_xpath)))
    except TimeoutException:  # Invalid number
        return None
    try:
        status = text(driver)
        filename = screenshot(driver, savedir, phone)
        if not filename:
            return None
        else:
            return filename, status
    except ElementClickInterceptedException:
        return None