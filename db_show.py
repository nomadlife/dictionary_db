import sqlite3
conn = sqlite3.connect('engdic.sqlite')
c = conn.cursor()

# for row in c.execute('SELECT * FROM entries'):
#     print(row)


conn.commit()   
conn.close()