import glob
import os

import numpy as np
import telegram
from astropy.table import Table
from tqdm.auto import tqdm

BOT_TOKEN = os.environ.get('PEOPLE_API_TOKEN')


def telegram_upload(savedir, verbose=False, clear=False):
    bot = telegram.Bot(BOT_TOKEN)

    if verbose:
        print('\nSending images to Telegram...\n')

    files = glob.glob(savedir + '*.png')
    data = Table.read(savedir + 'data.csv')

    for file in tqdm(files):
        phone = file[-17:-4]
        phones = np.array(data['phone'])
        status = data[phones == phone]['status'][0]
        photo = open(file, 'rb')
        bot.send_photo('@peoplefinder',
                       photo=photo,
                       caption='Phone number: +{0} {1} {2}-{3}\n'
                               'Status: {4}\n'
                               'https://api.whatsapp.com/send?phone={5}'.format(
                                phone[0:2], phone[2:4], phone[4:9], phone[9:], status, phone),
                       timeout=60)
        if verbose:
            print('Sending {0}...'.format(phone))
        photo.close()
        if clear:
            os.remove(file)

    del bot
