import sqlite3


def connect_to_db():
    conn = sqlite3.connect("playlists.db")
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS playlists (id STRING PRIMARY KEY,name STRING , snapshot STRING,length INT)"
    )
    conn.commit()
    return conn, c


def add_to_db(id, name, snapshot, length):
    conn, c = connect_to_db()

    try:
        c.execute(
            f"INSERT INTO playlists (id,name, snapshot,length) VALUES (?,?,?,?)",
            (id, name, snapshot, length),
        )
    except sqlite3.IntegrityError:
        print("The playlist is already being tracked")

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


def get_last_length(id):
    conn, c = connect_to_db()
    c.execute("SELECT length FROM playlists WHERE id= id")
    length = c.fetchone()
    conn.close()
    return length[0]


connect_to_db()
