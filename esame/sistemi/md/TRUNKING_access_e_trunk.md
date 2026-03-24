# TRUNKING access e trunk
Il networking è fatto di equilibri: da una parte vogliamo ridondanza per evitare che la rete cada, dall'altra dobbiamo evitare che i pacchetti girino all'infinito creando dei "loop". Qui entrano in gioco i collegamenti **Trunk** e i protocolli **STP/RSTP**.

Ecco un'analisi dettagliata di come funzionano e del confronto tra le versioni dello Spanning Tree.

---

## 1. Il Ruolo del Trunk Link
Un link **Trunk** è un collegamento fisico (solitamente tra due switch o tra uno switch e un router) configurato per trasportare il traffico di **più VLAN** contemporaneamente su un singolo cavo. 

Senza i trunk, dovresti usare un cavo fisico per ogni singola VLAN, il che sarebbe inefficiente e costoso. Il protocollo standard utilizzato oggi è l'**IEEE 802.1Q**, che aggiunge un "tag" al frame Ethernet per identificare a quale VLAN appartiene quel traffico.

---

## 2. STP vs RSTP: L'evoluzione della stabilità
Lo Spanning Tree Protocol (STP) nasce per prevenire i loop di livello 2. Se colleghi due switch con due cavi diversi per sicurezza, i dati inizierebbero a rimbalzare tra i due creando un "broadcast storm" che blocca la rete. L'STP risolve il problema mettendo logicamente in "blocco" i percorsi ridondanti, attivandoli solo se il link principale fallisce.

### STP (Standard 802.1D)
È la versione originale. Funziona, ma è "lenta" per gli standard moderni. Quando avviene un guasto, la rete può impiegare dai **30 ai 50 secondi** per ricalcolare un nuovo percorso e riprendere a trasmettere.

* **Vantaggi:** Semplicità, bassissimo consumo di risorse della CPU dello switch, compatibilità universale con hardware datato.
* **Svantaggi:** Tempi di convergenza biblici. Trenta secondi di buio in una rete moderna significano chiamate VoIP cadute e sessioni database interrotte.

### RSTP (Rapid STP - 802.1w)
Come suggerisce il nome, è l'evoluzione rapida. Invece di aspettare passivamente dei timer fissi, RSTP usa un meccanismo di "proposta e accordo" tra gli switch per decidere chi deve bloccare cosa. La convergenza avviene solitamente in **meno di 2 secondi** (spesso millisecondi).

* **Vantaggi:** Velocità quasi istantanea; retrocompatibile con il vecchio STP; gestisce meglio i link "Edge" (quelli che vanno ai PC e non devono mai causare ricalcoli).
* **Svantaggi:** Leggermente più esigente in termini di risorse (ma trascurabile sugli switch attuali); in scenari molto complessi con hardware misto, la configurazione richiede più attenzione.

---

## 3. Tabella Comparativa

| Caratteristica | STP (802.1D) | RSTP (802.1w) |
| :--- | :--- | :--- |
| **Tempo di convergenza** | 30 - 50 secondi | < 2 secondi |
| **Stati della porta** | Blocking, Listening, Learning, Forwarding | Discarding, Learning, Forwarding |
| **Meccanismo** | Basato su timer fissi | Basato su interazione attiva (Handshake) |
| **Utilizzo moderno** | Deprecato (legacy) | Standard attuale per reti LAN |

---

## Conclusioni
Oggi non c'è una vera ragione tecnica per preferire il vecchio STP al **RSTP**, a meno che tu non stia lavorando su hardware degli anni '90. Il Trunk è il "tubo" che trasporta le VLAN, mentre l'RSTP è il "vigile urbano" che decide quale tubo aprire o chiudere per evitare incidenti, assicurandosi che se un tubo si rompe, ne venga aperto un altro in un battito di ciglia.

**Ti interessa approfondire come configurare un Trunk su un apparato specifico (ad esempio Cisco o HP) o vuoi sapere come si comportano questi protocolli in presenza di EtherChannel?**