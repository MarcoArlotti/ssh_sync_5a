# FIREWALL e tipi di FIREWALL
# La DMZ (Demilitarized Zone): Architettura e Strategie Sistemistiche

In ambito sistemistico e di sicurezza delle reti, la **DMZ (Demilitarized Zone)** rappresenta un segmento di rete isolato che funge da cuscinetto tra una rete locale (LAN) fidata e una rete esterna non fidata (tipicamente Internet).

L'obiettivo primario è esporre i servizi rivolti all'esterno senza compromettere l'integrità della rete interna.

---

## 1. Concetto e Funzionamento
Il termine, mutuato dal gergo militare, indica una zona neutrale. In informatica, la DMZ ospita server che devono essere accessibili da utenti esterni, come server Web, Email o DNS.

Se un attaccante riesce a compromettere un server nella DMZ, rimane comunque confinato in quel segmento: il firewall impedirà (o limiterà drasticamente) l'accesso dalla DMZ verso la rete interna (LAN).



---

## 2. Architetture Comuni
Esistono due approcci principali per implementare una DMZ lato sistemistico:

### A. Firewall a Tre Gambe (Triple-Homed Firewall)
Un singolo firewall fisico o virtuale possiede almeno tre interfacce di rete:
1.  **Esterna:** Connessa a Internet.
2.  **DMZ:** Dove risiedono i server pubblici.
3.  **Interna:** Connessa alla LAN aziendale.

> **Vantaggio:** Gestione centralizzata delle policy e costi ridotti.

### B. Firewall Back-to-Back (Dual Firewall)
Si utilizzano due firewall in serie:
* Il **Firewall Esterno** permette il traffico da Internet solo verso la DMZ.
* Il **Firewall Interno** permette il traffico solo dalla DMZ verso specifici servizi della LAN (es. database) e viceversa.

> **Vantaggio:** Massima sicurezza; se un firewall viene violato, l'attaccante deve ancora superare un secondo dispositivo (spesso di un produttore diverso per evitare vulnerabilità comuni).

---

## 3. Utilizzi e Servizi Tipici
Un amministratore di sistema colloca nella DMZ tutti i nodi "sacrificabili" o esposti:

* **Web Server (HTTP/HTTPS):** Per ospitare siti aziendali o portali clienti.
* **Mail Gateway:** Server che ricevono la posta esterna prima di inoltrarla al server Exchange/Postfix interno.
* **Server DNS Esterni:** Per la risoluzione dei nomi dei servizi pubblici.
* **Proxy/Reverse Proxy:** Per bilanciare il carico e ispezionare il traffico applicativo.
* **Endpoint VPN:** Per terminare le connessioni remote prima di validare l'accesso alla LAN.

---

## 4. Best Practice Sistemistiche
Per una gestione efficace della DMZ, è fondamentale seguire alcuni principi di *Hardening*:

1.  **Isolamento dei Host:** I server nella DMZ non dovrebbero comunicare tra loro a meno che non sia strettamente necessario.
2.  **Policy "Default Deny":** Tutto il traffico è bloccato, tranne quello esplicitamente autorizzato.
3.  **No Dati Sensibili:** I database contenenti dati critici devono risiedere nella LAN interna. La DMZ deve interrogare il database tramite porte specifiche protette dal firewall.
4.  **Monitoraggio e Logging:** Essendo la zona più soggetta ad attacchi, i log della DMZ devono essere inviati a un server SIEM o syslog situato nella rete interna.

---

## Conclusioni
La DMZ è un pilastro della **Defense in Depth** (Difesa in Profondità). Non rende i server invulnerabili, ma limita il raggio d'azione di una possibile compromissione, proteggendo l'asset più prezioso: i dati e i client della rete interna.
