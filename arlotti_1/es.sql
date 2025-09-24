-- database: :memory:
CREATE TABLE Apicoltore (
    id INT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    cognome VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);

CREATE TABLE Miele (
    id INT PRIMARY KEY,
    denominazione VARCHAR(50) NOT NULL,
    Tipologia_Miele INT REFERENCES Tipologia_Miele(id)
);

CREATE TABLE Tipologia_Miele (
    id INT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

CREATE TABLE Apiario (
    codice VARCHAR(50) PRIMARY KEY,
    numero_arnire INT NOT NULL,
    localita VARCHAR(50) NOT NULL,
    comune VARCHAR(50) NOT NULL,
    provincia VARCHAR(50) NOT NULL,
    regione VARCHAR(50) NOT NULL,
    anno INT NOT NULL,
    quantita_prodotta FLOAT NOT NULL,
    Apicoltore_id INT REFERENCES Apicoltore(id),
    Miele_id INT REFERENCES Miele(id)
);

INSERT INTO Apicoltore (id,nome, cognome, email, password) VALUES
(0, "fabio", 'bila', 'fabiobila@gmail.com', "wdwdwd"),
(1, "matteo", 'massa', 'massamatto@gmail.com', "wdwdwd"),
(2, "luca", 'pontellini', 'lucaplasticiferroviari@gmail.com', "wdwdwd");

INSERT INTO Miele (denominazione,Miele_id) VALUES 
("millefiori"),
("acacia"),
("miele di castagno");

INSERT INTO Tipologia_Miele (nome) VALUES ("bila");
INSERT INTO Tipologia_Miele (nome) VALUES ("massa");
INSERT INTO Tipologia_Miele (nome) VALUES ("pontos");

INSERT INTO Apiario (numero_arnire, localita, comune, provincia, regione, anno, quantita_prodotta) VALUES (1, "napoli", "riccione", "scampia", "campania", 2025, 69.104);
INSERT INTO Apiario (numero_arnire, localita, comune, provincia, regione, anno, quantita_prodotta) VALUES (2, "napoli", "riccione", "scampia", "campania", 2024, 69.104);
INSERT INTO Apiario (numero_arnire, localita, comune, provincia, regione, anno, quantita_prodotta) VALUES (3, "napoli", "riccione", "scampia", "campania", 2021, 69.104);

SELECT nome FROM Apicoltore WHERE id = 1;
SELECT regione FROM Apiario WHERE regione = 'Lombardia';
SELECT id, numero_arnire FROM Apiario WHERE numero_arnire > 10;
SELECT id, localita FROM Apiario WHERE id = 2;
SELECT Miele_id FROM Tipologia_Miele WHERE id = 3;
SELECT denominazione FROM Miele WHERE id = 5;
SELECT Apiario WHERE anno = 2024;
SELECT Apiario WHERE codice = 'A001';
SELECT Miele_id FROM Tipologia_Miele WHERE id = 3 AND anno = 2023;