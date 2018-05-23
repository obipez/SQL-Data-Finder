import psycopg2


def get_top_three():
    
    cur.execute("SELECT title, count(log.time) FROM articles, log WHERE path LIKE concat('%', slug) "
                "GROUP BY title ORDER BY count(log.time) desc LIMIT 3;")

    rows = cur.fetchall()

    print("The top 3 articles and their views are: ")
    for i in rows:
        print('"' + i[0] + '"' + ' -- ' + str(i[1]) + ' views')

    conn.commit()
    

def most_popular_authors():
    
    cur.execute("SELECT authors.name, count(log.time) FROM articles, authors, log WHERE path LIKE concat('%', slug) and authors.name=articles.author GROUP BY authors.name ORDER BY count(log.time) desc LIMIT 4;")

    rows = cur.fetchall()

    print("The most popular authors and their views are: ")
    for i in rows:
        print(i[0] + ' -- ' + str(i[1]) + ' views')

    conn.commit()    
    
    
def percent_of_errors():

    cur.execute("SELECT authors.name, count(log.time) FROM articles, authors, log WHERE path LIKE concat('%', slug) and authors.name=articles.author GROUP BY authors.name ORDER BY count(log.time);")

    rows = cur.fetchall()

    print("The day where more than 1% of requests led to errors: ")
    for i in rows:
        print(i[0] + ' -- ' + str(i[1]) + '% errors')

    conn.commit()  
    
    
if __name__ == '__main__':
    conn = psycopg2.connect(database="news")

    cur = conn.cursor()

    get_top_three()
    most_popular_authors()
    percent_of_errors()

    conn.close()
