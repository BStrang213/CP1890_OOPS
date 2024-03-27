import sqlite3

DB_FILE = 'baseball_Player.sqlite'


def connect():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def close(conn):
    conn.close()
    print("Database closed")


def create_table(conn):
    cur = conn.cursor()
    query = ("CREATE TABLE IF NOT EXISTS Players (player_id INTEGER PRIMARY KEY, First_name TEXT, Last_Name TEXT, "
             "Position TEXT, At_Bats INTEGER, Hits INTEGER)")
    cur.execute(query)
    conn.commit()


def get_First(conn):
    print("Place Holder")


def get_Last(conn):
    print("Place Holder")


def get_Pos(conn):
    print("Place Holder")


def get_Bats(conn):
    print("Place Holder")


def Hits(conn):
    print("Place Holder")


def Average(conn):
    print("Place Holder")


if __name__ == "__main__":
    conn = connect()
