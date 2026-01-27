from app.db import get_db
from datetime import datetime

def get_comments_by_post(post_id):
    """Recupera un singolo post per ID (con JOIN per l'autore)."""
    db = get_db()
    query = """
        SELECT *
        FROM comment
        JOIN user ON comment.author_id = user.id
        WHERE post_id = ?;
    """

    post = db.execute(query, (post_id,)).fetchall()
    return post

def create_comment(post_id, author_id, body):
    db = get_db()
    db.execute('INSERT INTO comment (testo, post_id, author_id) VALUES(?,?,?,?)',
           (body, post_id, author_id))
    db.commit()
