#Connecting to a database
#Note: If the database does not exist, then this command will create the database


import psycopg2

conn = psycopg2.connect( user="postgres", password="pass", host="localhost", port="5432")


#The first step is to create a cursor. 
cur = conn.cursor()
cur.connection.set_isolation_level(0)
#create db
cur.execute("CREATE DATABASE tcount")
cur.close()
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
#Create a Table
cur.execute('''CREATE TABLE Tweetwordcount
       (word TEXT PRIMARY KEY     NOT NULL,
       count INT     NOT NULL);''')
conn.commit()
conn.close()


#Inserting/Selecting/Updating


cur = conn.cursor()

#Insert
cur.execute("INSERT INTO Tweetwordcount (word,count) \
      VALUES ('test', 1)");
conn.commit()

#Update
cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word=%s", (uWord, uCount))
conn.commit()

#Select
cur.execute("SELECT word, count from Tweetwordcount")
records = cur.fetchall()
for rec in records:
   print "word = ", rec[0]
   print "count = ", rec[1], "\n"
conn.commit()

conn.close()
