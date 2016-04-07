import psycopg2
import sys

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

cur = conn.cursor()

#print sys.argv[2]
cur.execute("SELECT word, count from Tweetwordcount  Where count between %s AND %s order by count desc", (sys.argv[1],sys.argv[2]))
records = cur.fetchall()

for rec in records:
                print  rec[0], ": ", rec[1]
