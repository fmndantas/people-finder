from astropy.table import Table


def save_data(savedir, phone, filename, status):
    try:
        data = Table.read(savedir + 'data.csv')
    except FileNotFoundError:
        data = Table(names=('phone', 'status', 'path'), dtype=('U19', 'U140', 'U{}'.format(len(savedir) + 17)))
    if phone in data['phone']:
        data[data['phone'] == phone]['status'] = status
        data[data['phone'] == phone]['path'] = filename
    else:
        data.add_row([phone, status, filename])

    data.write(savedir + 'data.csv', overwrite=True)

