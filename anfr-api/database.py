import psycopg2
from psycopg2 import OperationalError
import os

HOST = os.environ.get("POSTGRES_HOST") or "marcpartensky.com"
PORT = os.environ.get("POSTGRES_PORT") or "5433"
DATABASE = os.environ.get("POSTGRES_DB") or "db"
USER = os.environ.get("POSTGRES_USER") or "user"
PASSWORD = os.environ.get("POSTGRES_PASSWORD") or "password"

conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s port=%s" % (HOST, DATABASE, USER, PASSWORD, PORT))

def checkIfConnectionIsAlive(conn):
    try:
        conn.isolation_level
        return conn
    except OperationalError as oe:
        conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s port=%s" % (HOST, DATABASE, USER, PASSWORD, PORT))
        return conn