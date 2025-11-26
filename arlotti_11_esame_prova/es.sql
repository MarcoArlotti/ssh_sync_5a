-- database: :memory:
CREATE TABLE Typology (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(300)
);

CREATE TABLE Honey (
    id INT PRIMARY KEY,
    denomination VARCHAR(50) NOT NULL,
    typology_id INT,
    FOREIGN KEY (typology_id) REFERENCES Typology(id)
);

CREATE TABLE Beekeeper (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE Apiary (
    code INT PRIMARY KEY,
    num_hives INT NOT NULL,
    locality VARCHAR(300) NOT NULL,
    comune VARCHAR(300) NOT NULL,
    province VARCHAR(300) NOT NULL,
    region VARCHAR(300) NOT NULL,
    beekeeper_id INT,
    FOREIGN KEY (beekeeper_id) REFERENCES Beekeeper(id)
);

CREATE TABLE Production (
    id INT PRIMARY KEY,
    year INT,
    quantity FLOAT,
    apiary_code INT,
    honey_id INT,
    FOREIGN KEY (apiary_code) REFERENCES Apiary(code),
    FOREIGN KEY (honey_id) REFERENCES Honey(id)
);

-- Typology
INSERT INTO Typology (id, name, description) VALUES
(1, 'Monofloral', 'Miele prodotto prevalentemente da un unico fiore'),
(2, 'Polyfloral', 'Miele di millefiori, raccolto da più specie floreali'),
(3, 'Honeydew', 'Miele prodotto a partire dal melato (secrezioni di insetti)');

-- Beekeeper
INSERT INTO Beekeeper (id, name) VALUES
(1, 'Marco Rossi'),
(2, 'Lucia Bianchi'),
(3, 'Alessandro Verdi');

-- Honey
INSERT INTO Honey (id, denomination, typology_id) VALUES
(1, 'Acacia', 1),
(2, 'Castagno', 1),
(3, 'Millefiori', 2),
(4, 'Eucalipto', 2),
(5, 'Melata di Bosco', 3);

-- Apiary
INSERT INTO Apiary (code, num_hives, locality, comune, province, region, beekeeper_id) VALUES
(100, 12, 'Fattoria Le Rose', 'San Pietro', 'Pisa', 'Toscana', 1),
(101, 8, 'Colle Verde', 'Montevarchi', 'Arezzo', 'Toscana', 2),
(102, 20, 'Bosco Alto', 'Vercelli', 'Vercelli', 'Piemonte', 3),
(103, 5, 'Terrazza Sud', 'Verona', 'Verona', 'Veneto', 1);

-- Production
INSERT INTO Production (id, year, quantity, apiary_code, honey_id) VALUES
(1, 2022, 120.5, 100, 1),
(2, 2022, 95.2, 101, 3),
(3, 2023, 210.0, 102, 5),
(4, 2023, 34.7, 103, 2),
(5, 2024, 150.0, 100, 3),
(6, 2024, 78.3, 101, 4);

-- 4. le interrogazioni espresse in linguaggio SQL che restituiscono:
-- a) l’elenco degli apicoltori che producono miele DOP in una determinata regione;
-- b) il numero complessivo di apiari per ciascuna regione;
-- c) le quantità di miele prodotto in Italia lo scorso anno per ciascuna delle quattro tipologie

SELECT Honey.denomination, Apiary.region, beekeeper.id, beekeeper.name
FROM Production
JOIN Apiary ON Production.apiary_code = Apiary.code
JOIN Beekeeper ON Apiary.beekeeper_id = beekeeper.id
JOIN Honey ON Production.honey_id = Honey.id
WHERE Apiary.region = 'Toscana' AND Honey.denomination LIKE '%DOP%';

