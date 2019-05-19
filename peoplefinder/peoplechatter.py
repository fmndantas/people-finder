import glob
import logging
import os
import sqlite3
import time
import traceback
from tqdm.auto import tqdm

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from peoplefinder.SendData import send_text_data, send_image_data
from peoplefinder.csvcompat import getPhonesAndNames

home_dir = os.getenv('userprofile') + os.sep
save_dir = os.path.join(home_dir, 'peoplefinder' + os.sep)
photos_dir = os.path.join(save_dir, 'photos' + os.sep)

if not os.path.exists(save_dir):
    os.mkdir(save_dir)

if not os.path.exists(photos_dir):
    os.mkdir(photos_dir)


# if not os.path.exists(os.path.join(save_dir, 'data.db')):
#     conn = sqlite3.connect(os.path.join(save_dir, 'data.db'))
#     conn.execute("""
#         CREATE TABLE data (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#         phone TEXT,
#         status TEXT,
#         photo TEXT,
#         laststream TEXT);
#         """)
#     conn.close()


def login(debug_mode=False):
    default_profile = glob.glob(home_dir + 'AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*.default*')[0]
    options = Options()
    profile = FirefoxProfile(default_profile)
    if not debug_mode:
        options.add_argument('-headless')
    try:
        drvr = webdriver.Firefox(firefox_profile=profile, firefox_options=options)
        drvr.implicitly_wait(20)
    except Exception:
        logging.error(traceback.format_exc())
    else:
        return drvr


def routine(driver, csvfile_dir=glob.glob(os.path.join(save_dir, '*.xlsx'))[0], procedure='t'):
    print(save_dir)
    names, phones = getPhonesAndNames(csvfile_dir)
    if procedure == 't':
        for phone in phones:
            assert (type(phone) == str)
            assert (len(phone) in (10, 11))
            ddd, number = phone[:2], phone[2:]
            phone = '55{0}{1}'.format(ddd, number)
            msg = open(os.path.join(save_dir, 'stream.txt')).readlines()
            send_text_data(driver, phone, msg)
    elif procedure == 'i':
        for phone in tqdm(phones):
            assert (type(phone) == str)
            assert (len(phone) in (10, 11))
            ddd, number = phone[:2], phone[2:]
            phone = '55{0}{1}'.format(ddd, number)
            msg = open(os.path.join(save_dir, 'stream.txt')).readlines()
            send_image_data(driver, phone,
                            os.path.join(save_dir, glob.glob(os.path.join(save_dir, 'fk_test.*'))[0]),
                            msg)
    driver.close()


def main():
    driver = login()
    try:
        WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(('class name', '_3CSsZ')))
    except TimeoutException:
        driver.close()
    else:
        start = time.time()
        routine(driver, procedure='i')
        end = time.time()
        print('Tempo decorrido: ', end-start)


if __name__ == '__main__':
    main()