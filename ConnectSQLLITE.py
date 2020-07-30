import sqlite3

database1 = sqlite3.connect("test.db")

database1.execute("CREATE TABLE users (name text, email integer,age integer, userid integer)")


database1.close()