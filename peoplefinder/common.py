import glob
import os
import shutil
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

_HOME_ = os.getenv('userprofile')
_PACK_PARENT_ = Path(__file__).parent.parent

def make_dirs(platform):
    try:
        if platform in ('win32', 'win64'):
            print('Sample directories')
            for dir in os.listdir(os.path.join(_PACK_PARENT_, 'folders')):
                shutil.copytree(os.path.join(_PACK_PARENT_, 'folders'+os.sep+dir), os.path.join(_HOME_, dir))
    except FileExistsError:
        pass

def login(debug_mode):
    default_profile = glob.glob(_HOME_ + '\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*.default*')[0]
    options = Options()
    profile = FirefoxProfile(default_profile)
    if not debug_mode:
        options.add_argument('-headless')
    try:
        drvr = webdriver.Firefox(firefox_profile=profile, options=options)
        qr_code_xpath = '/html/body/div[1]/div/div/div[2]/div[1]/div/div[2]/div/img'
        WebDriverWait(drvr, 30).until_not(EC.presence_of_element_located((By.XPATH, qr_code_xpath)))
    except TimeoutError:
        print('No WhatsApp valid account identified. Your should log first...')
    else:
        return drvr

def get_dirs(path):
    dirs = [folder for folder in os.listdir(path) if os.path.isdir(os.path.join(path, folder))]
    return dirs

def purge_empty_dirs():
    PATH = os.path.join(_HOME_, 'peoplefinder')
    DIRS = get_dirs(PATH)
    for DIR in DIRS:
        if not os.listdir(os.path.join(PATH, DIR)):
            os.removedirs(os.path.join(PATH, DIR))