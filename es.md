```mermaid

erDiagram
    BEEKEEPER {
        int id PK "id_apicoltore"
        string name "nome"
    }

    TYPOLOGY {
        int id PK
        string name "nome_tipologia"
        string description
    }

    HONEY {
        int id PK
        string denomination "denominazione"
        int typology_id FK
    }

    APIARY {
        string code PK "codice_apiario"
        int num_hives "numero_arnie"
        string locality "località"
        string comune
        string province
        string region
        int beekeeper_id FK
    }

    PRODUCTION {
        int id PK
        int year "anno"
        float quantity "quantita_annua"
        int apiary_code FK
        int honey_id FK
    }

    %% Relationships
    BEEKEEPER ||--o{ APIARY : "possiede"
    TYPOLOGY ||--o{ HONEY : "classifica"
    HONEY ||--o{ PRODUCTION : "è_prodotto_in"
    APIARY ||--o{ PRODUCTION : "registra"
```