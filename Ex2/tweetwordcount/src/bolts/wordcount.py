from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import psycopg2



class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        self.conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT word, count from Tweetwordcount")
        self.records = self.cur.fetchall()


    def process(self, tup):
        word = tup.values[0]

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount
        # Table name: Tweetwordcount
        # you need to create both the database and the table in advance.

        for rec in self.records:
            self.counts[rec[0]] = int(rec[1])
        #First count all the words and  Increment the local count
        self.counts[word] += 1
        #Now this will create the pipeline
        self.emit([word, self.counts[word]])

        #only insert if it does not exist
        if self.counts[word]==1:
                self.cur.execute("INSERT INTO tweetwordcount (word,count) VALUES (%s, 1)", (word,));
        else:
        #updates all in our word list
				self.cur.execute("UPDATE tweetwordcount SET count = %s WHERE word = %s", (self.counts[word],word))
        self.conn.commit()
        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word])
