import psycopg2

HOST = "marcpartensky.com"
PORT = "5433"
DATABASE = "db"
USER = "user"
PASSWORD = "password"

conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s port=%s" % (HOST, DATABASE, USER, PASSWORD, PORT))
cur = conn.cursor()