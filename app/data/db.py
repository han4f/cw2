import sqlite3

def connect_database():
    conn = sqlite3.connect("cw2.db")
    return conn


if __name__ == "__main__":
    conn = connect_database()
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS cyber_incidents")
    cur.execute("DROP TABLE IF EXISTS datasets_metadata")
    cur.execute("DROP TABLE IF EXISTS it_tickets")
    cur.execute("DROP TABLE IF EXISTS users")

    conn.commit()
    conn.close()
    print("Database tables reset!")




