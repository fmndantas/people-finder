import os
from time import sleep

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def text(driver):
    """Get status"""
    header = driver.find_element_by_class_name('_2y17h')
    header.click()
    # wait until text has loaded in the sidebar
    while True:
        try:
            WebDriverWait(driver, 1).until(EC.text_to_be_present_in_element(('class name', '_14oqx'), 'Mute'))
        except TimeoutException:
            continue
        else:
            break
    texts = driver.find_elements_by_class_name('_14oqx')
    if len(texts) < 4:
        status = ''
    else:
        status = texts[2].text
    return status


def screenshot(driver, savedir, phone):
    # wait a little bit to load images
    sleep(3.0)
    picbox = driver.find_element_by_class_name('_2u2Mg')
    piclist = picbox.find_elements_by_tag_name('img')
    if len(piclist) == 0:
        filename = ''
    else:
        piclist[0].click()
        pic = driver.find_element_by_class_name('_1zH0g')
        filename = savedir + phone + '.png'
        pic.screenshot(filename)
    return filename


def get_data(driver, phone, savedir, stream):
    """Takes the photo and number of a given contact in WhatsApp"""
    if not stream:
        driver.get('https://web.whatsapp.com/send?phone={}'.format(phone))
        sleep(2.0)
        try:
            WebDriverWait(driver, 30).until_not(EC.presence_of_element_located(('class name', '_2dA13')))
        except TimeoutException:
            return None
    try:
        status = text(driver)
    except NoSuchElementException:
        return None

    photo_dir = os.path.join(savedir, 'photos' + os.sep)
    filename = screenshot(driver, photo_dir, phone)

    return filename, status
