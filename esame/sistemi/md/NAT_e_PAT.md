# NAT e PAT
Ecco un approfondimento tecnico su NAT e PAT, strutturato per un ambiente di rete aziendale.

---

# Configurazione e Implementazione di NAT e PAT in Rete Aziendale

In un contesto di networking moderno, la gestione degli indirizzi IPv4 richiede efficienza e sicurezza. NAT e PAT sono le tecnologie fondamentali che permettono a una rete privata di comunicare con l'esterno (Internet) utilizzando un numero limitato di indirizzi IP pubblici.

## 1. Definizioni e Differenze

### NAT (Network Address Translation)
Il NAT è un meccanismo che permette di modificare l'indirizzo IP nell'header di un pacchetto mentre attraversa un router o un firewall.
* **Static NAT:** Associa un indirizzo IP privato a un indirizzo IP pubblico in modo biunivoco (1:1). Viene usato principalmente per rendere accessibili server interni (es. Web o Mail server) dall'esterno.
* **Dynamic NAT:** Utilizza un pool di indirizzi pubblici. Quando un host interno richiede l'accesso a Internet, il router gli assegna temporaneamente uno degli indirizzi disponibili nel pool.

### PAT (Port Address Translation)
Il **PAT**, spesso chiamato "NAT Overload", è la forma più comune di NAT utilizzata nelle aziende.
* Permette a **molteplici host interni** di condividere un **singolo indirizzo IP pubblico**.
* Il router distingue le diverse sessioni assegnando a ciascuna un numero di porta sorgente univoco.
* Supporta fino a circa 65.000 sessioni contemporanee per singolo IP pubblico.



---

## 2. Architettura di Rete Aziendale

In una rete enterprise, l'implementazione segue solitamente una logica a zone:

1.  **Inside Local:** Gli indirizzi IP privati assegnati ai dispositivi nella LAN (es. `192.168.1.x`).
2.  **Inside Global:** L'indirizzo IP pubblico assegnato dal provider (ISP) che rappresenta la rete interna verso l'esterno.
3.  **Outside Global/Local:** Gli indirizzi di destinazione su Internet.

---

## 3. Guida all'Implementazione

L'implementazione avviene solitamente sul **Edge Router** o sul **Firewall** perimetrale. Ecco i passaggi logici per una configurazione standard (es. sintassi Cisco IOS):

### Fase A: Definizione delle Interfacce
Bisogna istruire il dispositivo su quale sia il lato "sicuro" (interno) e quello "insicuro" (esterno).
* `interface GigabitEthernet0/0` -> `ip nat inside`
* `interface GigabitEthernet0/1` -> `ip nat outside`

### Fase B: Configurazione del PAT (Overload)
È il metodo standard per permettere ai dipendenti di navigare su Internet.
1.  **Creare una ACL (Access Control List):** Per definire quali IP interni sono autorizzati a essere tradotti.
    ```bash
    access-list 1 permit 192.168.10.0 0.0.0.255
    ```
2.  **Attivare il NAT Overload:** Associare l'ACL all'interfaccia esterna.
    ```bash
    ip nat inside source list 1 interface GigabitEthernet0/1 overload
    ```

### Fase C: Configurazione NAT Statico (Port Forwarding)
Per permettere l'accesso a un server interno (es. un server web sulla porta 80):
```bash
ip nat inside source static tcp 192.168.10.50 80 203.0.113.5 80
```

---

## 4. Considerazioni su Sicurezza e Performance

* **Sicurezza (Security by Obscurity):** Il NAT non è un firewall, ma funge da barriera iniziale poiché nasconde la topologia della rete interna agli attaccanti esterni.
* **Logging:** In ambito aziendale è critico mantenere i log delle traduzioni NAT per finalità di audit e troubleshooting (sapere quale utente interno ha generato un determinato traffico verso l'esterno).
* **Resource Exhaustion:** Se il numero di connessioni simultanee è estremamente elevato, le tabelle NAT del router possono saturare la memoria RAM, causando rallentamenti o cadute di connessione.

---

## Tabella Comparativa

| Caratteristica | NAT Statico | NAT Dinamico | PAT (Overload) |
| :--- | :--- | :--- | :--- |
| **Rapporto IP** | 1:1 | M:N (Pool) | M:1 |
| **Uso Principale** | Server pubblici (DMZ) | Accesso temporaneo | Navigazione utenti (LAN) |
| **Risparmio IP** | Nullo | Moderato | Massimo |

---

Ti serve aiuto per generare i comandi di configurazione specifici per un particolare vendor (come Fortinet, Palo Alto o MikroTik)?