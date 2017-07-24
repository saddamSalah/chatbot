import sqlite3


def connect():
    conn = sqlite3.connect('DB.db')
    c = conn.cursor()
    return c,conn


# Design Clients table
def createTable(c):
    c.execute('''CREATE TABLE if not exists CLIENT(id INTEGER PRIMARY KEY,
     fullname text NOT NULL,
      age text,
       nationality text,
        work text)
        ''')


def insert(conn, c, record):

    for item in record:
        c.execute('INSERT INTO CLIENT VALUES (?,?, ?, ?, ?)', item)

    conn.commit()
    print" Your Info has been registered "




def selectAll(c):
    for row in c.execute('SELECT * FROM CLIENT'):
        print row


def close(conn):
    conn.close()

if __name__ =="__main__":
    c = connect()
    createTable(c)
