import psycopg2
import sys


conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

cur = conn.cursor()

#print sys.argv[2]
try:
 a = int(sys.argv[1])

 b = int(sys.argv[2])

 if(b<a):
  c=b
  d=a
 else:
  c=a
  d=b

 cur.execute("SELECT word, count from Tweetwordcount  Where count between %s AND %s order by count desc", (c,d))
 records = cur.fetchall()

 for rec in records:
                print  rec[0], ": ", rec[1]

except Exception as error:
 print("Please provide two numbers separated by space)")
