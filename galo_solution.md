```mermaid
erDiagram
    Negozi ||--o{ Dipendenti : "lavora"
    Negozi ||--o{ Scontrino : "effettua"
    Artisti ||--o{ AlbumVirtuale : "produce"
    Scontrino ||--o{ RigheScontrino : "dettaglia"
    RigheScontrino }o--|| AlbumVirtuale : "riguarda"
    RigheScontrino {
        INTEGER id PK
        INTEGER scontrino_id FK
        INTEGER album_id FK
        INTEGER quantita
    }

    %% Scontrino }o--o{ AlbumVirtuale : "puo essere venduto in"

    Negozi {
        INTEGER codice PK
        TEXT indirizzo
        TEXT citta
    }

    Dipendenti {
        INTEGER id PK
        TEXT nome
        TEXT cognome
        INTEGER negozio_id FK
    }

    Artisti {
        INTEGER id PK
        TEXT nome
        TEXT cognome
    }

    AlbumVirtuale {
        INTEGER codice PK
        TEXT titolo
        REAL prezzo
        REAL prezzo_unitario
        INTEGER artista_id FK
    }

    Scontrino {
        INTEGER id PK
        DATE data
        INTEGER negozio_id FK
        REAL importo_totale
    }
```