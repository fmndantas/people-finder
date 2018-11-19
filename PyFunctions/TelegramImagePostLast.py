import telegram
from telegram.error import TimedOut
import os
from time import sleep


def TelegramImagePost(temp_numbers):
    token = '683213671:AAHk6IN65mLZcvfYThxtg1a9PUXfdX1q_Og'
    bot = telegram.Bot(token = token)
    print('\nNow sending the images for Telegram...\n')
    
    i = 0
    while i < len(temp_numbers):
        try:
            photo = open('../People/{0}.png'.format(temp_numbers[i]),'rb')
            bot.send_photo('@imagesFromDisk',
                           photo = photo,
                           caption = '+{0} {1} {2}-{3}'.format(temp_numbers[i][0:2],
                                                               temp_numbers[i][2:4],
                                                               temp_numbers[i][4:9],
                                                               temp_numbers[i][9:len(temp_numbers[i])]))
            print('Sending {0}...'.format(temp_numbers[i]))
        except (TimedOut, FileNotFoundError) as exception:
            # print(exception)
            sleep(10)
            continue
        # except:
        #     i += 1
        else:
            photo.close()
            i += 1

    del(bot)

    sleep(5.0)

    """Removes sent numbers from data"""
    i = 0
    while i < len(temp_numbers):
        try:
            os.remove('../People/{0}.png'.format(temp_numbers[i]))
            sleep(1.0)
        except PermissionError as perr:
            print(perr)
            continue
        except:
            continue
        else:
            i += 1