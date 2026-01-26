from ..db import get_db
def get_categorie():
    db = get_db()
    query = """
        SELECT categoria.nome
        FROM categoria
        ORDER BY categoria.nome ASC;
    """
    rows = db.execute(query).fetchall()
    categorie = [row["nome"] for row in rows] #cava <sql3.row...>
    print("categorie fetched from database:", categorie)
    return categorie