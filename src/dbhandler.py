import sqlite3


def connect_to_db():
    conn = sqlite3.connect("playlists.db")
    c = conn.cursor()
    return conn, c


def create_table():
    conn, c = connect_to_db()
    c.execute(
        "CREATE TABLE IF NOT EXISTS playlists (id STRING PRIMARY KEY,name STRING , snapshot STRING)"
    )
    conn.commit()
    conn.close()


def add_to_db(id, name, snapshot):
    conn, c = connect_to_db()

    try:
        c.execute(
            f"INSERT INTO playlists (id,name, snapshot) VALUES (?,?,?)",
            (id, name, snapshot),
        )
    except sqlite3.IntegrityError:
        print("The database is already being tracked")

    conn.commit()
    conn.close()


def get_tracked_playlists():
    playlists = {}
    conn, c = connect_to_db()
    c.execute("SELECT id,name FROM playlists ")
    conn.commit()
    rows = c.fetchall()
    conn.close()

    for playlist in rows:
        playlists[playlist[1]] = playlist[0]
    return playlists


def get_last_snapshot(id):
    conn, c = connect_to_db()
    c.execute("SELECT snapshot FROM playlists WHERE id = id")
    last_snapshot = c.fetchone()
    conn.close()
    return last_snapshot[0]


# get_last_snapshot("46jC89e0qdF2FQnTin1VTj")
