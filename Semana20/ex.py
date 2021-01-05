import sqlite3

counts = dict()

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    split_mail = email.split("@")
    org = split_mail[1]
    counts[org] = counts.get(org, 0) + 1


# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'


vkcounts = [(value, key) for value, key in counts.items()]

for count in vkcounts:
    cur.execute('INSERT INTO Counts VALUES (?, ?)',
                (count[0], count[1]))

conn.commit()
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
cur.close()
