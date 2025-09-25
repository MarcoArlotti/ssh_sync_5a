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
(2, "luca", 'pontellini', 'plasticiferroviari@gmail.com', "wdwdwd");


INSERT INTO Tipologia_Miele (id, nome) VALUES
(1, "bila"),
(2, "massa"),
(3, "pontos");

INSERT INTO Miele (id,denominazione,Tipologia_Miele) VALUES 
(1, "millefiori",1),
(2, "acacia",1),
(3, "miele di castagno",3);

INSERT INTO Apiario (
codice,
numero_arnire,
localita,
comune,
provincia,
regione,
anno,
quantita_prodotta,
Apicoltore_id,
Miele_id
) VALUES
("vvdv", 18, "napoli", "riccione", "scampia", "campania", 2025, 69.104, 0, 1),
("sdfs", 22, "napoli", "riccione", "scampia", "campania", 2024, 104.104, 1, 2),
("fssf", 37, "napoli", "riccione", "scampia", "campania", 2021, 69.69, 2, 3);

SELECT SUM(quantita_prodotta) 
FROM apiario;

SELECT AVG(quantita_prodotta) 
FROM apiario;

SELECT SUM(quantita_prodotta)
FROM apiario
GROUP BY anno = 2024;

SELECT MAX(quantita_prodotta) 
FROM Apiario; 
SELECT MIN(quantita_prodotta) 
FROM Apiario;

SELECT quantita_prodotta
FROM Apiario
GROUP BY quantita_prodotta = 200;

