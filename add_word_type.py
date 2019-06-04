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


for i,d in enumerate(data):
    word = d[0]
    try:
        c.execute('SELECT word,wordtype FROM entries WHERE word=? collate nocase', (word,))
    except:
        print(word)
        sys.exit(2)

    record = c.fetchone()
    if record == None:
        d.append('')
    else:
        d.append(record[1])

    c.execute('SELECT word,wordtype,count(*) FROM entries WHERE word=? collate nocase group by wordtype order by count(*) desc', (word,))
    record = c.fetchone()
    if record == None:
        d.append('')
    else:
        d.append(record[1])
    if i < 50 or i%100==0:
        print(d)

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