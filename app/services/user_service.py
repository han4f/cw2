import bcrypt

def migrate_users_from_file(conn, filepath="DATA/users.txt"):
    cursor = conn.cursor()
    try:
        with open(filepath, "r") as f:
            for line in f:
                username, password_hash = line.strip().split(",")[:2]
                cursor.execute(
                    "INSERT OR IGNORE INTO users (username, password_hash) VALUES (?, ?)",
                    (username, password_hash)
                )
        conn.commit()
    except FileNotFoundError:
        pass


def register_user(username, password, conn, role="user"):
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        return False, "User already exists"

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    cursor.execute(
        "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
        (username, hashed, role)
    )
    conn.commit()
    return True, "User registered"


def login_user(username, password, conn):
    cursor = conn.cursor()

    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()

    if not row:
        return False, "User not found"

    if bcrypt.checkpw(password.encode(), row[0].encode()):
        return True, "Login successful"

    return False, "Wrong password"

