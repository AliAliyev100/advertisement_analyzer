import psycopg2
from psycopg2.extras import execute_values
class Database:
    def __init__(self):
        self.conn=psycopg2.connect(
        dbname="advertisement_analyzer",
        user="gadiraliyev",
        password="admin",
        host="localhost", 
        port="5432"  # 
        )
        self.cur = self.conn.cursor()

    def close_connection(self):
        self.cur.close()
        self.conn.close()

    def get_news_websites_from_database(self):
        query = "SELECT * FROM news_websites"
        self.cur.execute(query)
        news_websites = self.cur.fetchall()
        return news_websites
