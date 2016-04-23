import math
import psycopg2
import sys

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

cur = conn.cursor()


cur.execute("SELECT word, count from Tweetwordcount order by count desc limit 20")

records = cur.fetchall()
sumn = 0
hist = {}
for i, v in records:
    sumn += v
k=0
for i, v in records:
    k = math.ceil(float(v)/sumn *100)/2
    hist[i] = k
    print i, '          ',
    while (k>0):
        print "*",
        k = k -1
    print hist[i], "%"
