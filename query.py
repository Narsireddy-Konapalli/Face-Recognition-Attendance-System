import sqlite3
conn=sqlite3.connect('Attendance.db')
cursor=conn.cursor()

#To create a new table
"""
cursor.execute('''create table present_list(USNS text,
NAMES text,
SUBJECT text,
DATE text,
TIME text)''')

# To delete all records in table

cursor.execute("Delete from present_list")
"""
#To display all records in table
cursor.execute("select * from present_list")
records=cursor.fetchall()#fetchone,fetchmany(10)
for record in records:
    print(record)





"""with open('usns.txt', 'r') as file:
    usn_list = [line.strip() for line in file.readlines()]
    print(len(usn_list))
    usn_lst=usn_list[0].split(',')
    usn_list=usn_lst[:-1]
    print(usn_list)"""

conn.commit()
conn.close()


