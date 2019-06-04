import sqlite3, sys, csv

# if len(sys.argv) > 1:
#     # print(sys.argv[1])
#     word = sys.argv[1]
    
# else:
#     sys.exit('input word.')


conn = sqlite3.connect('engdic.sqlite')
c = conn.cursor()

with open('word_list_school1_test.csv', newline='') as csvfile:
    content = csv.reader(csvfile, delimiter=',', quotechar='"')
    data = list(content)
    # for row in data:
    #     print(', '.join(row))


for d in data[:100]:
    word = d[0]
    c.execute('SELECT word,wordtype,definition FROM entries WHERE word=? collate nocase', (word,))
    wordtype = c.fetchone()
    if wordtype == None:
        d.append('')
    else:
        d.append(wordtype[1])

    c.execute('SELECT word,wordtype,count(*) FROM entries WHERE (lower(word) LIKE ? ) group by wordtype ', (word,))
    wordtype = c.fetchone()
    if wordtype == None:
        d.append('')
    else:
        d.append(wordtype[1])

with open('word_list_school1_test_result.csv', 'w', newline='') as myfile:
     writer = csv.writer(myfile, quoting=csv.QUOTE_MINIMAL)
     for line in data:
            writer.writerow(line)
    #  writer.writerow(data)

# for row in c.execute('SELECT word,wordtype,definition FROM entries WHERE word=? collate nocase', (word,)):
#     print(row)

# c.execute('SELECT word,wordtype,definition FROM entries WHERE word=? collate nocase', (word,))
# print(c.fetchone()[1])

conn.commit()   
conn.close()