import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

#cursor.execute('CREATE TABLE user (id varchar(20) primary key, name varchar(20))')

#cursor.execute('INSERT INTO user (id, name) values (\'7\', \'claude\')')

print(cursor.rowcount)

cursor.execute('SELECT * FROM user WHERE id=2')

values = cursor.fetchall()

print(values)

cursor.close()

conn.commit()

conn.close()
