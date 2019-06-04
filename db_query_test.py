import sqlite3, sys

if len(sys.argv) > 1:
    # print(sys.argv[1])
    word = sys.argv[1]
    
else:
    sys.exit('input word')


conn = sqlite3.connect('engdic.sqlite')
c = conn.cursor()



# for row in c.execute('SELECT word,wordtype,definition FROM entries WHERE word=? collate nocase', (word,)):
#     print(row)

# for row in c.execute('SELECT word,wordtype,count(*) FROM entries WHERE word=? collate nocase group by wordtype', (word,)):
#     print(row)

c.execute('SELECT word,wordtype,definition,count(*) FROM entries WHERE word=? collate nocase group by wordtype', (word,))
record = c.fetchone()
print(record)
print(record[1])


# c.execute('SELECT word,wordtype,definition FROM entries WHERE word=? collate nocase', (word,))
# print(c.fetchone()[1])

conn.commit()   
conn.close()