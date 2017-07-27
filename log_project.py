#!/usr/bin/env python3

import psycopg2

DBNAME = "news"

def queryDB(sql):
    """Return the result of the sql-query"""
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(sql)
        result = c.fetchall()
        db.close()
    except IOError:
        print("Could not connect to database!")

    return result

# Answer of 1st Question
sql = """
  SELECT title, count(slug) AS views FROM articles
  INNER JOIN log ON articles.slug = substr(log.path, 10, LENGTH(log.path)-1)
  GROUP BY title ORDER BY views DESC LIMIT 3;"""

print("1. What are the most popular three articles of all time?")
results = queryDB(sql)
for row in results:
    print ("%s -- %d views" % (row[0], row[1]))
print


# Answer of 2nd Question
sql = """
  SELECT name, count(slug) AS views FROM (articles
  INNER JOIN log ON articles.slug = substr(log.path, 10, LENGTH(log.path)-1))
  INNER JOIN authors ON authors.id = articles.author
  GROUP BY name ORDER BY views DESC;"""


print("2. Who are the most popular article authors of all time?")
results = queryDB(sql)
for row in results:
    print ("%s -- %d views" % (row[0], row[1]))
print

# Answer of 3rd Question
sql = """
  SELECT date(time) AS day,
  CAST (SUM(case WHEN status='200 OK' THEN 0 ELSE 1 END)
  AS FLOAT)/COUNT(*) AS error FROM log GROUP BY day
  HAVING (CAST (SUM(CASE WHEN status='200 OK' THEN 0 ELSE 1 END)
  AS FLOAT)/COUNT(*) ) > 0.01;"""

print("3. On which days did more than 1 Percent of requests lead to errors?")
results = queryDB(sql)
for row in results:
    print ("%s -- %d%% request error" % (row[0], row[1] * 100))
