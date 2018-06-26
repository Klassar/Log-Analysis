Log Analysis
=============

# Using this code..
### To use cd into the vagrant directory
### Type vagrant up
### Type vagrant ssh
### cd into /vagrant/log_analysis
### Run python myPythonScript.py
### Celebrate!


## First Query Output
### To get the 3 most popular articles of all time i CONCAT '/article/ to the articles.slug so it will match the path column from log. From there I can join them and group by the articles slug column and ORDER by the time count in a desceding order, at which point i limit the return by 3 to get the top 3 articles.
### "SELECT articles.slug AS articles, count(log.time) AS views FROM articles JOIN log ON CONCAT('/article/', articles.slug) = log.path GROUP BY articles.slug ORDER BY count(log.time) DESC LIMIT 3;"

### Second Query Output
### Very similar to the first query here i changed what the select statement was returning to show data from the authors table this time. Then i added a second join from the articles.author to the authors.id to display the authors name and count from log.time.
### "SELECT authors.name AS authors, count(log.time) AS views FROM articles JOIN log ON CONCAT('/article/', articles.slug) = log.path JOIN authors ON articles.author = authors.id GROUP BY authors.name ORDER BY count(log.time) DESC;"

### Third Query Output
### Struggled here, my final query returns time in DATE format and the status count multiplied by 1,000,000.0 from statuses that do not have the status of '200 OK' to return a decimal number above 1 divided by the origional status count. From here i limited the output to 27 as to only show dates and errors that are above 1%.

### Ideally it would return the 27 programmatically but i could not find how to set that conditional inside a WHERE clause.

### "SELECT DATE(time), CONCAT(COUNT(status) * 1000000.0 / (SELECT COUNT(status) FROM log), '%', ' errors' ) AS errors FROM log WHERE status != '200 OK' GROUP BY time ORDER BY COUNT(status) DESC LIMIT 27;"
