import psycopg2
from psycopg2 import OperationalError

HOST = "marcpartensky.com"
PORT = "5433"
DATABASE = "db"
USER = "user"
PASSWORD = "password"

conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s port=%s" % (HOST, DATABASE, USER, PASSWORD, PORT))

def checkIfConnectionIsAlive(conn):
    try:
        conn.isolation_level
        return conn
    except OperationalError as oe:
        conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s port=%s" % (HOST, DATABASE, USER, PASSWORD, PORT))
        return conn