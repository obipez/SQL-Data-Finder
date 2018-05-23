import psycopg2


def get_top_three():
    
    cur.execute("""SELECT title, count(log.time) FROM articles, log WHERE path LIKE concat('%', slug) 
                GROUP BY title ORDER BY count(log.time) desc LIMIT 3;""")

    rows = cur.fetchall()
    
    print
    print("The top 3 articles and their views are: ")
    for i in rows:
        print('"' + i[0] + '"' + ' -- ' + str(i[1]) + ' views')
    print

    conn.commit()
    
    rows = cur.fetchall()
    
    
def most_popular_authors():
    
    cur.execute("""SELECT authors.name, count(log.time)
                FROM articles, authors, log WHERE path 
                LIKE concat('%', slug) and authors.id = articles.author 
                GROUP BY authors.name ORDER BY count(log.time) desc LIMIT 4;""")

    rows = cur.fetchall()
    
    print("The most popular authors and their views are: ")
    for i in rows:
        print(i[0] + ' -- ' + str(i[1]) + ' views')
    print

    conn.commit()    

    
def percent_of_errors():
    
#    cur.execute("""CREATE VIEW total AS
#            SELECT date(time), COUNT(*) AS views
#            FROM log
#            GROUP BY date(time)
#            ORDER BY date(time);""")
#    
#    cur.execute("""CREATE VIEW err AS
#            SELECT date(time), COUNT(*) AS errors
#            FROM log WHERE status LIKE '404%'
#            GROUP BY date(time)
#            ORDER BY date(time);""")
    
    cur.execute("""SELECT total.date, ((100.0*err.errors/total.views)>1)
            AS percent 
            FROM total, err
            WHERE total.date = err.date
            ORDER BY percent DESC LIMIT 1;""")
    
    rows = cur.fetchall()
    
    print("The day where more than 1% of requests led to errors: ")
    for i in rows:
        print(" %s -- %s error" % (i[0], i[1]))
    print

    conn.commit()
    
    
if __name__ == '__main__':
    conn = psycopg2.connect(database="news")

    cur = conn.cursor()

    get_top_three()
    most_popular_authors()
    percent_of_errors()

    conn.close()
