# "Database code" for the DB Forum.

import psycopg2

# Query for Question 1.
db = psycopg2.connect("dbname=news")
c = db.cursor()
query = "SELECT articles.slug AS articles, count(log.time) AS views FROM articles JOIN log ON CONCAT('/article/', articles.slug) = log.path GROUP BY articles.slug ORDER BY count(log.time) DESC LIMIT 3;"
c.execute(query)
output = c.fetchall()
print(output)
db.close()

# Query for Question 2.
db = psycopg2.connect("dbname=news")
c = db.cursor()
query = "SELECT authors.name AS authors, count(log.time) AS views FROM articles JOIN log ON CONCAT('/article/', articles.slug) = log.path JOIN authors ON articles.author = authors.id GROUP BY authors.name ORDER BY count(log.time) DESC;"
c.execute(query)
output = c.fetchall()
print(output)
db.close()
    

# Query for Question 3.
# Divdies status count
db = psycopg2.connect("dbname=news")
c = db.cursor()
query = "SELECT DATE(time), CONCAT(COUNT(status) * 1000000.0 / (SELECT COUNT(status) FROM log), '%', ' errors' ) AS errors FROM log WHERE status != '200 OK' GROUP BY time ORDER BY COUNT(status) DESC LIMIT 27;"
c.execute(query)
output = c.fetchall()
print(output)
db.close()
