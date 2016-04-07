import psycopg2
import sys

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

cur = conn.cursor()

if len(sys.argv) > 1:
        cur.execute("SELECT word, count from Tweetwordcount Where word = %s", [sys.argv[1]])
        records = cur.fetchall()
        print "Total number of occurences are", records[0][1]

else:
        cur.execute("SELECT word, count from Tweetwordcount order by count desc limit 50")

        records = cur.fetchall()
        for rec in records:
                print  rec[0], ": ", rec[1]
