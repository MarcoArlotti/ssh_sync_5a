
import os
import sqlite3
import re

# 📁 Percorsi dinamici
base_folder = os.path.dirname(os.path.abspath(__file__))
sql_files_folder = os.path.join(base_folder, "folder_for_SQL_files")
python_files_folder = os.path.join(base_folder, "folder_for_Python_files")
db_path = os.path.join(base_folder, "db.sqlite")
db_log_path = os.path.join(base_folder, "db_paths.txt")

# 🛠️ Funzioni di gestione database
def crea_database_se_manca():
    if not os.path.exists(db_path):
        try:
            conn = sqlite3.connect(db_path)
            conn.close()
            print("✅ Database creato all'avvio.")
        except Exception as e:
            print(f"❌ Errore nella creazione del database: {e}")
    else:
        print("ℹ️ Il database esiste già.")

def elimina_database():
    if os.path.exists(db_path):
        try:
            os.remove(db_path)
            print("🧹 Database eliminato.")
        except PermissionError:
            print("❌ Il file db.sqlite è aperto da un altro programma. Chiudilo e riprova.")
            exit()

def elimina_tutti_i_database_sqlite():
    estensioni_valide = [".sqlite", ".db"]
    for root, _, files in os.walk(base_folder):
        for file in files:
            if any(file.endswith(ext) for ext in estensioni_valide):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"🧹 Eliminato: {file_path}")
                except PermissionError:
                    print(f"❌ Impossibile eliminare {file_path}: è aperto da un altro programma.")

def elimina_database_in_cartelle(cartelle):
    estensioni_valide = [".sqlite", ".db"]
    for folder in cartelle:
        print(f"\n🔍 Cerco database in: {folder}")
        for root, _, files in os.walk(folder):
            for file in files:
                if any(file.endswith(ext) for ext in estensioni_valide):
                    file_path = os.path.join(root, file)
                    try:
                        os.remove(file_path)
                        print(f"🧹 Eliminato: {file_path}")
                    except PermissionError:
                        print(f"❌ Impossibile eliminare {file_path}: è aperto da un altro programma.")
                    except Exception as e:
                        print(f"⚠️ Errore con {file_path}: {e}")

def elimina_database_da_lista(file_lista):
    if not os.path.exists(file_lista):
        print("📭 Nessun file di log trovato per i database Python.")
        return
    with open(file_lista, "r", encoding="utf-8") as f:
        percorsi = set(line.strip() for line in f if line.strip())
    for path in percorsi:
        if os.path.exists(path):
            try:
                os.remove(path)
                print(f"🧹 Eliminato da log: {path}")
            except Exception as e:
                print(f"❌ Errore con {path}: {e}")
    try:
        os.remove(file_lista)
        print(f"🧹 File di log eliminato: {file_lista}")
    except Exception as e:
        print(f"⚠️ Errore nell'eliminazione del file di log: {e}")

def ricrea_database():
    try:
        conn = sqlite3.connect(db_path)
        print("✅ Database ricreato correttamente.")
        return conn
    except Exception as e:
        print(f"❌ Errore nella creazione del database: {e}")
        return None

# 🔍 Analisi SQL
def controlla_sql(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().strip()
    if not content:
        print("⚠️ Il file SQL è vuoto.")
        return False
    keywords = ["CREATE TABLE", "INSERT INTO", "SELECT", "UPDATE", "DELETE"]
    trovati = [kw for kw in keywords if kw.lower() in content.lower()]
    if not trovati:
        print("⚠️ Nessuna istruzione SQL rilevante trovata.")
        return False
    print(f"🔍 Il file contiene: {', '.join(trovati)}")
    return True

def riepilogo_tabelle(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    if not tables:
        print("📭 Nessuna tabella presente nel database.")
        return
    print("\n📊 Tabelle nel database:")
    for table_name in [t[0] for t in tables]:
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor.fetchone()[0]
        print(f"   - {table_name}: {count} righe")

def estrai_tabelle_da_sql(sql_text):
    pattern = r"\b(?:FROM|JOIN|UPDATE|INSERT INTO)\s+([a-zA-Z_][a-zA-Z0-9_]*)"
    return list(set(re.findall(pattern, sql_text, re.IGNORECASE)))

def check_tabelle_presenti(conn, tabelle_richieste):
    cursor = conn.cursor()
    cursor.execute("SELECT LOWER(name) FROM sqlite_master WHERE type='table';")
    tabelle_presenti = [row[0] for row in cursor.fetchall()]
    return [t for t in tabelle_richieste if t.lower() not in tabelle_presenti]

# 📦 Monitoraggio dei database creati da script Python
def rileva_nuovi_database(prima, dopo):
    return [f for f in dopo if f not in prima]

def lista_database_in_cartelle(cartelle):
    estensioni = [".db", ".sqlite"]
    db_files = []
    for folder in cartelle:
        for root, _, files in os.walk(folder):
            for file in files:
                if any(file.endswith(ext) for ext in estensioni):
                    db_files.append(os.path.abspath(os.path.join(root, file)))
    return db_files

# 🚀 Avvio
print("📂 Il database verrà resettato solo quando esegui un file SQL.")
print(f"📍 Percorso del database: {db_path}")
crea_database_se_manca()

python_eseguito = False

while True:
    try:
        sql_files = [f for f in os.listdir(sql_files_folder) if f.endswith(".sql")]
    except FileNotFoundError:
        print(f"❌ Cartella dei file SQL non trovata: {sql_files_folder}")
        break

    try:
        py_files = [f for f in os.listdir(python_files_folder) if f.endswith(".py")]
    except FileNotFoundError:
        print(f"❌ Cartella dei file Python non trovata: {python_files_folder}")
        py_files = []

    if not sql_files and not py_files:
        print("📭 Nessun file SQL o Python trovato.")
        break

    print("\n📄 File disponibili:")
    file_menu = [("sql", f) for f in sql_files] + [("py", f) for f in py_files]
    for i, (tipo, nome) in enumerate(file_menu, 1):
        icona = "📄" if tipo == "sql" else "🐍"
        print(f"{i}. {icona} {nome}")

    scelta = input("\nInserisci il numero del file da eseguire (o 'esci' per uscire): ").strip()
    if scelta.lower() == "esci":
        break
    if not scelta.isdigit():
        print("❌ Inserimento non valido.")
        continue

    scelta_index = int(scelta) - 1
    if not (0 <= scelta_index < len(file_menu)):
        print("❌ Numero fuori intervallo.")
        continue

    tipo_file, nome_file = file_menu[scelta_index]

    if tipo_file == "py":
        cartelle_monitorate = [
            base_folder,
            os.path.join(base_folder, "Computer_science"),
            os.path.join(base_folder, "New_exercises_with_database")
        ]
        db_prima = lista_database_in_cartelle(cartelle_monitorate)

        os.system(f"python3 \"{os.path.join(python_files_folder, nome_file)}\"")
        python_eseguito = True

        db_dopo = lista_database_in_cartelle(cartelle_monitorate)
        nuovi_db = rileva_nuovi_database(db_prima, db_dopo)

        if nuovi_db:
            with open(db_log_path, "a", encoding="utf-8") as log_file:
                for db in nuovi_db:
                    log_file.write(db + "\n")
                    print(f"📌 Database rilevato e registrato: {db}")
        continue

    file_path = os.path.join(sql_files_folder, nome_file)

    if not controlla_sql(file_path):
        conferma = input("Vuoi comunque eseguire il file? (sì/no): ").strip().lower()
        if conferma not in ["sì", "si", "y", "yes"]:
            print("⏭️ File saltato.")
            continue

    elimina_database()
    conn = ricrea_database()
    if conn is None:
        continue

    cursor = conn.cursor()

    with open(file_path, "r", encoding="utf-8") as f:
        sql_script = f.read()
        tabelle_richieste = estrai_tabelle_da_sql(sql_script)
        try:
            cursor.executescript(sql_script)
        except Exception as e:
            print(f"\n❌ Errore durante l'esecuzione: {e}")
            conn.close()
            continue

        tabelle_mancanti = check_tabelle_presenti(conn, tabelle_richieste)
        if tabelle_mancanti:
            print("\n🚫 Il file è stato eseguito, ma alcune tabelle richieste non sono presenti:")
            for tabella in tabelle_mancanti:
                print(f"❌ Tabella mancante: {tabella}")
        else:
            print(f"\n✅ {nome_file} eseguito con successo.")
            print("✅ Tutte le tabelle necessarie sono presenti.")

    riepilogo_tabelle(cursor)
    conn.commit()
    conn.close()

# 🔚 Fine sessione: pulizia completa
if python_eseguito:
    print("\n🧹 Pulizia finale dei database creati dagli script Python...")
    elimina_tutti_i_database_sqlite()

    cartelle_da_pulire = [
        os.path.join(base_folder, "New_exercises_with_database"),
        os.path.join(base_folder, "Computer_science"),
    ]
    elimina_database_in_cartelle(cartelle_da_pulire)
    elimina_database_da_lista(db_log_path)

print("\n👋 Fine sessione. Tutti i database .sqlite e .db sono stati eliminati.")

#esempio: avvio questo script e chiedo di aprire il 3. mi si genera scuola.db , ma quando scrivo "esci" scuola.db rimane dov'è e non si elimina.
#possibili idee: tracciare la locazione del file database generato dal singolo file python oppure usare il nome del database creato per eliminarlo quando si esce (in questo caso il 3)
#sistemare la grammatica, le frasi, il modo di capire cosa succede quando eseguo questo script perchè non si capisce bene il tutto