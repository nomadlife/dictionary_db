import sqlite3, sys

if len(sys.argv) > 1:
    # print(sys.argv[1])
    word = sys.argv[1]
    
else:
    sys.exit('input word')


conn = sqlite3.connect('engdic.sqlite')
c = conn.cursor()

with open('ws2.txt') as f:
    data = [line.rstrip() for line in f.readlines()]

# for row in c.execute('SELECT word,wordtype,definition FROM entries WHERE word=? collate nocase', (word,)):
#     print(row)

c.execute('SELECT word,wordtype,definition FROM entries WHERE word=? collate nocase', (word,))
print(c.fetchone()[1])

conn.commit()   
conn.close()