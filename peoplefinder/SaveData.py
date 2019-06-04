import os
import numpy as np
from astropy.table import Table
import sqlite3

def create_data_set(_SAVEDIR_):
    if not os.path.exists(os.path.join(_SAVEDIR_, 'data.db')):
        conn = sqlite3.connect(os.path.join(_SAVEDIR_, 'data.db'))
        conn.execute("""
            CREATE TABLE data (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            phone TEXT,
            status TEXT,
            photo TEXT);
            """)
        conn.close()

def save_data(savedir, phone, filename, status):
    create_data_set(savedir)
    conn = sqlite3.connect(os.path.join(savedir, 'data.db'))
    cursor = conn.cursor()
    fetch = cursor.execute("""SELECT phone FROM data""")
    if (phone,) in fetch.fetchall():
        cursor.execute("""
        UPDATE data
        SET status = ?, phone = ?
        WHERE phone = ?
        """, (status, filename, phone))
    else:
        cursor.execute("""INSERT INTO data (phone, status, photo)
        VALUES (?, ?, ?)""", (phone, status, filename))
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

