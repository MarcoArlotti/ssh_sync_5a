# crittografia simmetrica e assimetrica
# Crittografia Simmetrica e Asimmetrica: Architettura e Implementazione di Rete

La crittografia rappresenta il pilastro fondamentale della sicurezza informatica moderna. Dal punto di vista sistemistico, non si tratta solo di "nascondere dati", ma di garantire tre principi chiave: **Riservatezza**, **Integrità** e **Autenticità**.

---

## 1. Crittografia Simmetrica (Private Key Encryption)

La crittografia simmetrica utilizza una **singola chiave condivisa** sia per la cifratura che per la decifratura dei dati. È il metodo più antico e performante.

### Caratteristiche Tecniche
* **Velocità:** Estremamente elevata, ideale per il trasferimento di grandi moli di dati.
* **Algoritmi comuni:** AES (Advanced Encryption Standard), ChaCha20, 3DES.
* **Il problema della distribuzione:** Il limite principale è lo scambio della chiave. Se la chiave viene intercettata durante la trasmissione, l'intero canale è compromesso.



---

## 2. Crittografia Asimmetrica (Public Key Encryption)

Si basa su una **coppia di chiavi** matematicamente correlate ma diverse: la **Chiave Pubblica** (distribuibile a chiunque) e la **Chiave Privata** (segreta e custodita dal proprietario).

### Meccanismo di Funzionamento
1.  **Cifratura:** Ciò che viene cifrato con la chiave pubblica può essere decifrato solo dalla corrispondente chiave privata.
2.  **Firma Digitale:** Ciò che viene cifrato con la chiave privata può essere decifrato da chiunque possieda la chiave pubblica, garantendo l'autenticità del mittente.

### Caratteristiche Tecniche
* **Complessità:** Molto più lenta rispetto alla simmetrica a causa di calcoli matematici complessi (fattorizzazione di numeri primi o curve ellittiche).
* **Algoritmi comuni:** RSA, ECC (Elliptic Curve Cryptography), Diffie-Hellman.



---

## 3. Confronto Sistemistico

| Caratteristica | Simmetrica | Asimmetrica |
| :--- | :--- | :--- |
| **Chiavi** | Una sola chiave condivisa | Coppia di chiavi (Pubblica/Privata) |
| **Velocità** | Molto veloce | Lenta |
| **Utilizzo Risorse** | Basso (CPU/RAM) | Elevato |
| **Scopo Primario** | Riservatezza di grandi file/stream | Scambio chiavi e Firme digitali |

---

## 4. Utilizzi in Ambito Sistemistico e di Rete

Nella pratica quotidiana di un amministratore di sistema, queste due tecnologie non sono alternative, ma **complementari**. Spesso vengono utilizzate insieme in un sistema "ibrido".

### A. Protocollo TLS/SSL (HTTPS, FTPS)
È l'esempio più comune di sistema ibrido:
1.  Si usa la **crittografia asimmetrica** per autenticare il server e scambiarsi in modo sicuro una "chiave di sessione".
2.  Una volta stabilita la connessione, si passa alla **crittografia simmetrica** usando quella chiave per proteggere il traffico dati effettivo (molto più veloce).

### B. SSH (Secure Shell)
Fondamentale per la gestione remota dei server:
* Le **chiavi asimmetriche** (RSA/Ed25514) sostituiscono o integrano le password per l'accesso.
* Il tunnel di comunicazione viene poi protetto da algoritmi simmetrici.

### C. VPN (Virtual Private Networks)
Sia in IPsec che in OpenVPN/WireGuard:
* Si utilizzano algoritmi asimmetrici per il "handshake" iniziale e la mutua autenticazione tra i peer.
* Il flusso di dati del tunnel viene cifrato simmetricamente per minimizzare la latenza.

### D. Firma e Integrità dei Log
L'uso di chiavi asimmetriche permette di firmare i file di log o i backup. Questo assicura che, in caso di violazione, un attaccante non possa modificare i log per coprire le proprie tracce senza rompere la firma digitale.

---

## Considerazioni sulla Sicurezza
Dal punto di vista sistemistico, la sicurezza non dipende solo dall'algoritmo, ma dalla **gestione delle chiavi**:
* **Rotazione delle chiavi:** Cambiare periodicamente le chiavi simmetriche.
* **Key Storage:** Utilizzare moduli HSM (Hardware Security Module) o Vault software per proteggere le chiavi private.
* **Lunghezza della chiave:** Preferire oggi AES-256 e RSA almeno a 3072 bit (o meglio ECC).

Vorresti che approfondissi la configurazione pratica di uno di questi servizi (ad esempio come generare e gestire le chiavi per l'accesso SSH)?