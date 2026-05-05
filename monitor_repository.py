from database import get_connection

def insert_site(url):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO sites (url) VALUES (?)", (url,))
    conn.commit()
    conn.close()

def get_sites():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, url FROM sites")
    rows = cursor.fetchall()

    conn.close()

    resultado = []
    for r in rows:
        resultado.append({
            "id": r[0],
            "url": r[1]
        })

    return resultado

def get_site_by_id(site_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, url FROM sites WHERE id=?", (site_id,))
    row = cursor.fetchone()

    conn.close()

    if not row:
        return None

    return {
        "id": row[0],
        "url": row[1]
    }

def insert_check(site_id, status, tempo, data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO checks (site_id, status, tempo, data) VALUES (?, ?, ?, ?)",
        (site_id, status, tempo, data)
    )

    conn.commit()
    conn.close()

def get_checks_by_site(site_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT status, tempo, data FROM checks WHERE site_id=?",
        (site_id,)
    )

    rows = cursor.fetchall()
    conn.close()

    resultado = []
    for r in rows:
        resultado.append({
            "status": r[0],
            "tempo": r[1],
            "data": r[2]
        })

    return resultado