import sqlite3

database1 = sqlite3.connect("test.db")
crsr = database1.cursor()
crsr.execute("CREATE TABLE IF NOT EXISTS users (name text, email integer,age integer, userid integer)")
crsr.close()