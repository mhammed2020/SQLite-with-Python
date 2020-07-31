import sqlite3

database1 = sqlite3.connect("test4.db")
crsr = database1.cursor()
crsr.execute("CREATE TABLE IF NOT EXISTS users (userid integer, name text)")


#inserting data
# crsr.execute("insert into users (userid, name ) values (1,'Mhammed')")
# crsr.execute("insert into users (userid, name ) values (2,'Saber')")

l = ["jeddou","saber","allal","kamal","al haj", "imrane"]

for key,user in enumerate(l):
    crsr.execute(f"insert into users (userid, name ) values ({key+1},'{user}')")
database1.commit()
database1.close()