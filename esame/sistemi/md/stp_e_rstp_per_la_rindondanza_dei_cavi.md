# stp e rstp per la rindondanza dei cavi
Il **Spanning Tree Protocol (STP)** e la sua evoluzione, il **Rapid Spanning Tree Protocol (RSTP)**, sono i guardiani silenziosi delle reti locali (LAN). Senza di loro, il semplice collegamento di un cavo di troppo potrebbe causare il collasso totale di un'intera infrastruttura aziendale.

Ecco un'analisi tecnica del perché esistono e di come si sono evoluti.

---

## 1. Il problema: I Loop di Livello 2
A differenza dei pacchetti IP (Livello 3), i frame Ethernet non hanno un campo **TTL (Time To Live)**. Se un frame entra in un loop fisico tra switch, continuerà a circolare all'infinito.

Le conseguenze sono disastrose:
* **Broadcast Storm:** I messaggi di broadcast (come le richieste ARP) si moltiplicano esponenzialmente, saturando la banda.
* **Instabilità della Tabella MAC:** Lo switch continua a vedere l'indirizzo MAC di un dispositivo spostarsi da una porta all'altra, rendendo impossibile il switching corretto.



---

## 2. STP (IEEE 802.1D) - Il Classico
L'obiettivo dello Spanning Tree è creare una topologia logica a **albero** (senza cicli) all'interno di una rete fisica che presenta ridondanze.

### Come funziona
Il protocollo elegge un "capo" e decide quali strade chiudere:
1.  **Elezione del Root Bridge:** Lo switch con il **Bridge ID** più basso (priorità + indirizzo MAC) diventa il riferimento della rete.
2.  **Elezione delle Root Port:** Ogni switch non-root sceglie la porta con il percorso meno costoso verso il Root Bridge.
3.  **Elezione delle Designated Port:** Per ogni segmento di rete, viene scelta la porta che offre il miglior percorso verso il root.
4.  **Blocco delle altre porte:** Tutte le porte rimanenti vengono messe in stato di **Blocking**.

### Il limite del tempo
Il difetto principale dell'STP classico è la lentezza. Quando avviene un guasto, il protocollo deve passare attraverso vari stati:
* **Listening** (15s)
* **Learning** (15s)
* **Forwarding**
Il tempo di convergenza totale può arrivare a **30-50 secondi**, un'eternità per le applicazioni moderne (VoIP, Video, Database).

---

## 3. RSTP (IEEE 802.1w) - L'Evoluzione
Il Rapid STP è stato introdotto per risolvere i tempi di attesa biblici del predecessore, portando la convergenza a **pochi secondi** (spesso sotto i 2 secondi).

### Le innovazioni principali
* **Ruoli delle porte aggiuntivi:** Introduce la **Alternate Port** (una scorta pronta all'uso se la Root Port fallisce) e la **Backup Port**.
* **Stati semplificati:** Riduce gli stati da cinque a tre: *Discarding*, *Learning*, e *Forwarding*.
* **Meccanismo di Proposal/Agreement:** Invece di aspettare passivamente i timer, gli switch RSTP "parlano" tra loro attivamente per confermare che una porta può passare in Forwarding immediatamente.
* **Edge Ports:** Le porte collegate a PC o server (che non possono causare loop) vengono configurate come "Edge" e passano istantaneamente in Forwarding (PortFast).



---

## Confronto Rapido

| Caratteristica | STP (802.1D) | RSTP (802.1w) |
| :--- | :--- | :--- |
| **Tempo di convergenza** | 30 - 50 secondi | < 2 secondi |
| **Stati della porta** | 5 (Blocking, Listening, Learning, Forwarding, Disabled) | 3 (Discarding, Learning, Forwarding) |
| **Ruoli della porta** | Root, Designated, Non-designated | Root, Designated, Alternate, Backup |
| **Interazione** | Basata su timer passivi | Basata su handshake attivo |

---

## Conclusione
Mentre l'STP ha gettato le basi per la ridondanza di rete, l'**RSTP è lo standard de facto** nelle reti moderne. Oggi è raro trovare implementazioni del 802.1D puro; quasi tutti i produttori (Cisco, HP, Juniper) utilizzano varianti di RSTP o protocolli più avanzati come il **MSTP** (Multiple Spanning Tree), che permette di gestire alberi diversi per diverse VLAN.

**Ti interessa approfondire come configurare questi protocolli su uno switch specifico o vuoi sapere come funzionano le varianti per VLAN (PVST+)?**