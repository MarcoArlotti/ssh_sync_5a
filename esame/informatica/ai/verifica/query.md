Capisco perfettamente: bando alle ciance teoriche e passiamo subito al "come si fa". Quando parliamo di **query** (interrogazioni al database), solitamente ci riferiamo al linguaggio SQL.

Ecco una carrellata di esempi pratici, dai fondamentali fino a quei trucchetti "particolari" che risolvono i problemi veri.

---

## 1. Il Pane e il Burro: Filtri e Ordinamento

Iniziamo con una selezione classica. Immagina una tabella `Utenti`.

```sql
SELECT nome, cognome, email
FROM Utenti
WHERE data_iscrizione > '2023-01-01'
ORDER BY cognome ASC;

```

* **Cosa fa:** Prende solo tre colonne dei nuovi iscritti dal 2023 e li mette in ordine alfabetico.

---

## 2. Il "Trucco" del LIKE (Ricerca Flessibile)

Spesso non cerchi una parola esatta, ma un pezzo di essa.

```sql
SELECT * FROM Prodotti 
WHERE nome_prodotto LIKE '%Smartphone%';

```

* **Particolarità:** Il simbolo `%` è un jolly. Scritto così, trova "Smartphone Apple", "Cover Smartphone" o semplicemente "Smartphone". Se metti `%` solo alla fine (`Smart%`), cercherà solo parole che *iniziano* con "Smart".

---

## 3. Aggregazioni: Contare e Sommare

Se vuoi sapere quanto stai incassando, non ti servono i singoli record, ma il totale.

```sql
SELECT categoria, COUNT(*) as numero_prodotti, SUM(prezzo) as valore_totale
FROM Magazzino
GROUP BY categoria
HAVING valore_totale > 1000;

```

* **La cosa particolare:** `HAVING`. Molti provano a usare `WHERE` per filtrare i risultati sommati, ma non si può. `WHERE` filtra le righe singole, `HAVING` filtra i gruppi (in questo caso, solo le categorie che valgono più di 1000€).

---

## 4. Unire i puntini: La JOIN

I dati sono quasi sempre divisi in più tabelle. Colleghiamo `Ordini` e `Clienti`.

```sql
SELECT Clienti.nome, Ordini.id_ordine, Ordini.totale
FROM Clienti
INNER JOIN Ordini ON Clienti.id_cliente = Ordini.id_cliente;

```

* **Cosa succede:** La query "appiccica" le righe delle due tabelle dove l'ID del cliente combacia.

---

## 5. Cose Particolari: Le Subquery e i CASE

Qui entriamo nel territorio dei "pro".

### La Subquery (Query dentro la Query)

Vuoi trovare tutti i prodotti che costano più della media?

```sql
SELECT nome_prodotto, prezzo
FROM Prodotti
WHERE prezzo > (SELECT AVG(prezzo) FROM Prodotti);

```

* **Perché è speciale:** Non puoi scrivere `WHERE prezzo > AVG(prezzo)` direttamente. Devi prima far calcolare la media alla "sotto-query" tra parentesi.

### Il CASE (La logica "If-Then" in SQL)

Vuoi etichettare i dati mentre li estrai?

```sql
SELECT nome_prodotto, prezzo,
  CASE 
    WHEN prezzo > 100 THEN 'Costoso'
    WHEN prezzo BETWEEN 50 AND 100 THEN 'Medio'
    ELSE 'Economico'
  END AS fascia_prezzo
FROM Prodotti;

```

* **Particolarità:** Crei una colonna virtuale (`fascia_prezzo`) che non esiste nel database, ma viene generata al volo in base alle tue regole.

---

## 6. Gestire i duplicati (DISTINCT)

Se vuoi sapere quali città sono presenti nel tuo database senza vederle ripetute mille volte:

```sql
SELECT DISTINCT citta 
FROM Clienti;

```

* **Risultato:** Se hai 500 clienti a Roma, "Roma" apparirà una volta sola.

---

> **Consiglio da esperto:** Quando scrivi query, scrivi sempre le parole chiave (SELECT, FROM, WHERE) in **MAIUSCOLO**. Il database le capisce lo stesso se sono minuscole, ma i tuoi colleghi umani ti ringrazieranno per la leggibilità!