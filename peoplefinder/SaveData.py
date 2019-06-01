import os
import numpy as np
from astropy.table import Table
import sqlite3

def save_data(savedir, phone, filename, status, stream):
    conn = sqlite3.connect(os.path.join(savedir, 'data.db'))
    cursor = conn.cursor()
    fetch = cursor.execute("""SELECT phone FROM data""")
    # TODO: data exists but not the table
    if (phone,) in fetch.fetchall():
        cursor.execute("""
        UPDATE data
        SET status = ?, phone = ?, laststream = ?
        WHERE phone = ?
        """, (status, filename, stream, phone))
    else:
        cursor.execute("""INSERT INTO data (phone, status, photo, laststream)
        VALUES (?, ?, ?, ?)""", (phone, status, filename, stream))
        conn.commit()
    conn.close()


def save_data_astropy(savedir, phone, filename, status):
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

