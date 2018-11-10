#!/usr/bin/env python
import psycopg2


class Questions:


    dbname = "news"

    def __init__(self):


        try:
            self.db = psycopg2.connect(database=self.dbname)
            self.cursor = self.db.cursor()
        except Exception:
            return 'can not connect to the database'

    def popularArticle(self):


        print('What are the most popular three articles of all time?')
        self.cursor.execute("""
        select title, count(*) as views
            from articles inner join log
            on log.path like concat('/article/', articles.slug, '%')
            group by log.path, articles.title
            order by views desc limit 3;
            """)
        result = self.cursor.fetchall()
        for e, e2 in result:
            print '.', e, '---', e2, 'views'

    def popularAuthors(self):


        print('Who are the most popular article authors of all time?')
        self.cursor.execute("""
        select authors.name, count(*) as views
            from articles inner join authors
            on articles.author = authors.id inner join log
            on log.path like concat('/article/', articles.slug, '%')
            group by authors.name
            order by views desc;
            """)
        result = self.cursor.fetchall()
        for e, e2 in result:
            print '.', e, '---', e2, 'views'


    def error(self):


        print('On which days did more than 1% of requests lead to errors?')
        self.cursor.execute("""
        select day, percent from (
           select day, round((sum(errorReqs)/
           (select count(*) from log where date("time") = day)
           * 100), 2) as percent from
           (select date("time") as day,
           count(*) as errorReqs from log
           where status = '404 NOT FOUND' group by day)
           as logPercentage group by day order by percent desc) as finalQ
           where percent >= 1.0
           """)
        result = self.cursor.fetchall()
        for e, e2 in result:
            print '.', e, '---', e2, '% errors'

    def destroyConnection(self):


        self.db.close()

if __name__ == '__main__':
    Questions = Questions()
    Questions.popularArticle()
    print ''
    Questions.popularAuthors()
    print ''
    Questions.error()
    print ''
    Questions.destroyConnection()
