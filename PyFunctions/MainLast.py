from DataRegisterLast import DataRegister
from TelegramImagePostLast import TelegramImagePost
from GetPhotoLast import GetPhoto
import random
import shelve
from selenium import webdriver
import sys
import os
import progressbar
from time import sleep

if __name__ == "__main__":

    while True:
        try:
            data = shelve.open('../Shelve/peopleData') #import data
        except:
            os.makedirs('../Shelve')
            continue
        else:
            break

    data = shelve.open('../Shelve/peopleData') # import or creates data

    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com')

    input('Press enter once you have logged in... ')
    try:
        i = data['last_indice'] # pic indice
    except KeyError:
        i = 1 
    else:
        pass

    j = sys.argv[1] # quantity of independent loops
    send = sys.argv[2] # choose between send and no send the pics
    ddd = sys.argv[3] # phone ddd
    k = 0 # counter to reach j
    numbers = list()

    while k < int(j):
        print('{0}/{1} => {2:.1f}%'.format(str(k+1), j, (k+1)/int(j)*100))
        number = '55{1}999{0}'.format(random.randint(100000, 999999), ddd)
        #number = '1010' #used for tests
        control = GetPhoto(driver, number, i)
        if control != None:
            i += 1
            k += 1
            numbers.append(number)
        else:
            k += 1

    DataRegister(data, numbers, i)

    driver.close()

    if int(send) == 1:
        TelegramImagePost(data['temp_numbers'])
        data['temp_numbers'] = list()
    else:
        pass

    data.close()