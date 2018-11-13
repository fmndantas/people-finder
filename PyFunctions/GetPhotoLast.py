from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import os

# _3q4NP : common screen, to get into the decision screen

# _15JHr : no account case

# _18tv- : upper_frame object

# _1WliW : expande profile photo

# _3ZW2E : raises WebDriveException to photo case

def GetPhoto(driver, number, photo_indices):
    """ Takes the photo and number given a contact in whatsapp """
    """ GetPhoto(Photo, number, photo_indices) """

    if 'People' not in os.listdir('..'): # Creates people dir, if it doesn't exists yet
        os.makedirs('../People')
    else:
        pass

    driver.set_window_size(height=1000, width=600)
    driver.get('https://wa.me/{0}'.format(number))

    while True:
        try:
            send_message = driver.find_element_by_class_name('button--simple')
            send_message.click()
            element = WebDriverWait(driver, timeout=5).until(
                lambda driver: driver.find_element_by_class_name('_3q4NP'))
        except NoSuchElementException:
            send_message.click()
            print('except NoSuchElementException')
            continue
        except:
            print('except')
            continue
        else:
            print('else') # found send message button in common screen
            break

    sleep(1.0)

    # Two cases:
    # (1. No account)
    try:
        no_account = driver.find_element_by_class_name('_15JHr')
    except NoSuchElementException:
        pass
    else:
        print('No account case')
        return None

    upper_frame = driver.find_element_by_class_name('_18tv-')
    upper_frame.click()
    sleep(1.0)

    # (2. No photo)
    try:
        no_photo = driver.find_element_by_class_name('_3ZW2E')
        no_photo.click()
    except WebDriverException:
        photo = driver.find_element_by_class_name('_1WliW')
        photo.click()
        driver.set_window_size(height=1000, width=600)
        #os.makedirs('./People')
        driver.get_screenshot_as_file(
            '../People/{0}.png'.format(str(number)))
        print('Screenshot OKAY')
        return True
    else:
        print('No photo case')
        return None
