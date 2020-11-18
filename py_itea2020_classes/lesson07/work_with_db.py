import sqlite3

connect = sqlite3.connect('my_sqlite_database.db')
cursor = connect.cursor()
# cursor.execute('select * from parking')
#
# #print(cursor.fetchall())
#
# print(cursor.fetchmany(2))
# print(cursor.fetchmany(2))
# print(cursor.fetchmany(2))
# print(cursor.fetchmany(2))

#cursor.execute('insert into parking(price, model) values (15000, "tesla")')
#connect.commit()

id_ = input()

#cursor.execute(f'select * from parking where id={id_}')
cursor.execute(f'select * from parking where id=?',(id_,))
#print(cursor.fetchone())
while cursor:
    #print(cursor.fetchmany(2))
    result = cursor.fetchmany(2)
    if not result:
        break
    print(result)

cursor.close()