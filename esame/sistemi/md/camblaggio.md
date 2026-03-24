# camblaggio
Il cablaggio, in ambito sistemistico, non è semplicemente "stendere cavi", ma rappresenta l'infrastruttura critica (il **Layer 1** dello stack OSI) su cui poggia l'intera affidabilità di un data center o di una rete aziendale. Un sistema progettato male a livello fisico vanifica anche la configurazione software più sofisticata.

Ecco un’analisi strutturata del tema dal punto di vista sistemistico.

---

## 1. Il Concetto di Cablaggio Strutturato
Il sistemista moderno non ragiona per singoli collegamenti "punto-punto", ma per **cablaggio strutturato**. Si tratta di una rete di permutazione flessibile che permette di spostare servizi e dispositivi senza dover ricablare l'intero edificio.

* **Punti di Distribuzione (Rack/MDF/IDF):** Dove convergono i cavi provenienti dalle postazioni (orizzontali) e dai collegamenti tra piani (verticali/backbone).
* **Patch Panel:** L'interfaccia critica. Permette di collegare una porta fisica a uno switch specifico semplicemente spostando un "patch cord", mantenendo l'ordine e riducendo l'usura delle porte degli apparati attivi.



---

## 2. Standard e Tipologie di Supporto
La scelta del mezzo trasmissivo dipende dalle distanze e dalle prestazioni richieste ($10$ Gbps, $40$ Gbps o $100$ Gbps).

### Rame (Twisted Pair)
Ancora lo standard per le LAN (Local Area Network) grazie ai costi contenuti e alla tecnologia **PoE (Power over Ethernet)**, che permette di alimentare access point e telefoni VoIP direttamente dal cavo dati.
* **Cat 6/6A:** Supportano fino a $10$ Gbps (la 6A su distanze maggiori).
* **Schermatura (UTP vs STP):** Fondamentale in ambienti industriali con forti interferenze elettromagnetiche (EMI).

### Fibra Ottica
Essenziale per il **Backbone** (dorsale) e per le connessioni all'interno del Data Center (Storage, Server ad alte prestazioni).
* **Multimodale (OM3/OM4/OM5):** Ideale per brevi distanze (entro i $300$-$500$ metri).
* **Monomodale (OS2):** Per distanze chilometriche e larghezze di banda quasi illimitate.

---

## 3. Topologie e Architetture di Data Center
In ambito sistemistico avanzato, il modo in cui i cavi collegano i server cambia radicalmente le performance:

* **Top-of-Rack (ToR):** Ogni rack ha il suo switch in cima. I server si collegano con cavi corti (spesso DAC - Direct Attach Copper) allo switch del rack, e solo pochi uplink in fibra vanno al core della rete. **Vantaggio:** Meno cavi lunghi, più ordine.
* **End-of-Row (EoR):** I server di un'intera fila convergono verso un rack centrale di aggregazione. **Vantaggio:** Gestione centralizzata degli switch, ma "mare" di cavi sotto il pavimento flottante.
* **Spine-Leaf:** L'architettura moderna per il traffico "Est-Ovest" (tra server). Ogni switch "Leaf" (foglia) è collegato a ogni switch "Spine" (spina), garantendo latenza minima e ridondanza totale.



---

## 4. Best Practice Sistemistiche: L'Ordine è Efficienza
Un sistemista esperto valuta la qualità di un cablaggio da tre fattori non funzionali:

1.  **Gestione Termica:** Cavi ammassati e disordinati ostruiscono il flusso d'aria (Airflow). In un rack, questo porta al surriscaldamento degli apparati e al thermal throttling.
2.  **Manutenibilità e Troubleshooting:** Se un cavo fallisce, deve essere identificabile in pochi secondi. L'uso di etichette univoche e codici colore (es: Rosso per WAN, Blu per LAN, Giallo per Management) è vitale.
3.  **Raggio di Curvatura:** Forzare la piega di un cavo (specialmente in fibra) altera le proprietà fisiche e causa perdita di segnale o rotture permanenti.

---

## 5. Il Futuro: Software Defined e Velocità
Oggi il cablaggio deve supportare la velocità di evoluzione del software. Tecniche come l'**MPO/MTP** (connettori multifibra che portano 12 o 24 fibre in un unico spinotto) permettono di scalare rapidamente verso i $400$ Gbps richiesti dalle infrastrutture AI e Cloud moderne.

> **Nota di riflessione:** Un errore comune è risparmiare sul cablaggio per investire nel software. È un paradosso: un'interfaccia di rete da $1000$ euro è inutile se collegata a un cavo di categoria inadeguata o crimpato male.

---

Ti interessa approfondire le differenze tecniche tra i connettori (come LC, SC o RJ45) o preferiresti vedere uno schema su come organizzare logicamente le VLAN su un cablaggio fisico esistente?