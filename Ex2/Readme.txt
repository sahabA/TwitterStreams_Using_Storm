

1)Scripts work with Python 2.7, PostgreSQL, Tweepy, and Streamparse.

2) Run pycopg-sample.py to create a database and a table for storing tweet results

3) Run command 'sparse run' in the folder tweetwordcount to fill the tweetwordcount table we created in step2 with the live stream of tweeted words.

4) Run these mini scripts:

finalresults.py : Shows top 50 words with most wordcount. If an argument is provided, it looks for that word in the tabe and return it's word count

histogram.py : Takes two numeric arguments and bring all the words that has the count same and inbetween them. The order of the numbers do not matter. It also let the user know if they provide a non integer.

plot.py:Create a CLI histogram for the twenty word counts with most count using ' * '

5) Screenshots and plots are in images folder
