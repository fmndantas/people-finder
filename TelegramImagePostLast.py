import telegram
from telegram.error import TimedOut
import os
from time import sleep
import progressbar

def TelegramImagePost(temp_numbers):
    token = '683213671:AAHk6IN65mLZcvfYThxtg1a9PUXfdX1q_Og'
    bot = telegram.Bot(token = token)
    print('\nNow sending the images for Telegram...\n')
    
    i = 0
    while i < len(temp_numbers):
        try:
            bot.send_photo('@imagesFromDisk', photo = open('C:/Users/Fernando Dantas/PyCharmProjects/PeopleFinder/People/{0}.png'.format(temp_numbers[i]),'rb'), caption = '+{0} {1} {2}-{3}'.format(temp_numbers[i][0:2], temp_numbers[i][2:4], temp_numbers[i][4:9], temp_numbers[i][9:len(temp_numbers[i])]))
            print('Sending {0}...'.format(temp_numbers[i]))
        except (TimedOut, FileNotFoundError):
            i += 1
        except:
            i += 1
        else:
            i += 1

    del(bot)
    sleep(5.0)
    i = 0
    while i < len(temp_numbers):
        try:
            os.remove('C:/Users/Fernando Dantas/PyCharmProjects/PeopleFinder/People/{0}.png'.format(temp_numbers[i]))
        except PermissionError:
            print('PermissionError')
            continue
        except:
            continue 
        else:
            i += 1

