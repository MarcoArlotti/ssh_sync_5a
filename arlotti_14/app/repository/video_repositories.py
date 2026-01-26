from ..db import get_db
def get_videos(canale_id):
    db = get_db()
    query = """
        SELECT *
        FROM video
        JOIN 
        WHERE canale_id = ?
        ORDER BY titolo;
    """
    videos = db.execute(query, (canale_id,)).fetchall()
    print("Channels fetched from database:", videos)
    return [dict(video) for video in videos]
def get_categorie():
    db = get_db()
    query = """
        SELECT *
        FROM video
        WHERE canale_id = ?
        ORDER BY titolo;
    """
    categorie = db.execute(query, ()).fetchall()
    print("categorie fetched from database:", categorie)
    return categorie