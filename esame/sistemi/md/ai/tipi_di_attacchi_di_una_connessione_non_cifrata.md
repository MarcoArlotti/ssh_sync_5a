# tipi di attacchi di una connessione non cifrata
Proteggere una rete informatica oggi non è più solo una questione di "installare un antivirus", ma di costruire una strategia di difesa a più livelli. Gli attacchi sono diventati sofisticati, spesso mescolando vulnerabilità tecniche e psicologia umana.

Ecco un'analisi dei principali attacchi di rete e le strategie per neutralizzarli.

---

## 1. Malware (Software Malevolo)
Il malware è un termine generico che include virus, worm, trojan e, soprattutto, **Ransomware**. Quest'ultimo cripta i file della vittima e richiede un riscatto per la decrittazione.

* **Come avviene:** Spesso tramite allegati email, download da siti non sicuri o vulnerabilità del software non patchate.
* **Come prevenirlo:** * Utilizzare soluzioni **Endpoint Detection and Response (EDR)** anziché semplici antivirus.
    * Mantenere i sistemi operativi e i software costantemente aggiornati (Patch Management).

## 2. Phishing e Ingegneria Sociale
Questo attacco non colpisce l'hardware, ma l'anello più debole della catena: l'**essere umano**.

* **Come avviene:** L'attaccante invia comunicazioni (email, SMS, chiamate) fingendosi un'entità affidabile (banca, collega, supporto tecnico) per rubare credenziali o dati sensibili.
* **Come prevenirlo:**
    * Implementare l'**Autenticazione a Due Fattori (MFA)**: anche se l'attaccante ha la password, non può accedere senza il secondo codice.
    * Formazione continua dei dipendenti (Security Awareness Training).

## 3. Attacchi Man-in-the-Middle (MitM)
In un attacco MitM, l'hacker si inserisce segretamente tra due parti che comunicano (ad esempio, tra il tuo computer e il server della banca) per intercettare o alterare i dati.



* **Come avviene:** Spesso tramite reti Wi-Fi pubbliche non protette o tecniche di "spoofing" (fingersi un router legittimo).
* **Come prevenirlo:**
    * Utilizzare protocolli di crittografia come **HTTPS** e **TLS**.
    * Utilizzare una **VPN** quando ci si connette a reti esterne per creare un tunnel criptato.

## 4. Denial of Service (DoS) e DDoS
L'obiettivo non è rubare dati, ma rendere la rete o il servizio inutilizzabile sovraccaricandolo di traffico.

* **Come avviene:** Un attacco **Distributed DoS (DDoS)** utilizza una rete di computer infetti (Botnet) per inondare un server di richieste contemporaneamente.
* **Come prevenirlo:**
    * Configurare firewall e router per filtrare il traffico anomalo.
    * Utilizzare servizi di protezione cloud (come Cloudflare o AWS Shield) che assorbono i picchi di traffico.

## 5. SQL Injection (SQLi)
Questo attacco mira ai database che supportano i siti web e le applicazioni di rete.

* **Come avviene:** L'attaccante inserisce codice malevolo nei campi di input (come un modulo di login) per costringere il database a rivelare dati riservati o a cancellare tabelle.
* **Come prevenirlo:**
    * Sanificazione degli input (non fidarsi mai di ciò che l'utente scrive).
    * Utilizzo di query preparate e parametri (Parameterized Queries).

---

### Tabella Riassuntiva: Difesa in Profondità

| Livello di Difesa | Strumento/Tecnica | Obiettivo |
| :--- | :--- | :--- |
| **Perimetro** | Firewall & IPS/IDS | Monitorare e bloccare traffico sospetto in entrata. |
| **Identità** | MFA (Multi-Factor Auth) | Impedire l'accesso non autorizzato con credenziali rubate. |
| **Dati** | Crittografia (AES/RSA) | Rendere i dati illeggibili se intercettati. |
| **Resilienza** | Backup Offline/Immutabile | Ripristinare i sistemi in caso di attacco Ransomware. |

---

### La regola d'oro: Il principio del "Zero Trust"
La strategia moderna più efficace è il modello **Zero Trust** (Fiducia Zero). Invece di fidarsi di chiunque sia "dentro" la rete aziendale, questo approccio verifica l'identità di ogni utente e dispositivo a ogni singola richiesta di accesso, indipendentemente da dove provenga.

**Ti interessa approfondire come configurare un firewall o come implementare l'autenticazione a due fattori per la tua rete?**