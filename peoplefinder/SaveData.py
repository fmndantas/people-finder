import numpy as np
from astropy.table import Table


def save_data(savedir, phone, filename, status):
    try:
        data = Table.read(savedir + 'data.csv')
    except FileNotFoundError:
        data = Table(names=('phone', 'status', 'path'), dtype=('U13', 'U280', 'U{}'.format(len(savedir) + 17)))
        p0 = '-' * 13
        s0 = '-' * 280
        f0 = '-' * (len(savedir) + 17)
        data.add_row([p0, s0, f0])
    phones = np.array(data['phone'])
    if phone in data['phone']:
        data[phones == phone]['status'] = status
        data[phones == phone]['path'] = filename
    else:
        data.add_row([phone, status, filename])

    data.write(savedir + 'data.csv', overwrite=True)

