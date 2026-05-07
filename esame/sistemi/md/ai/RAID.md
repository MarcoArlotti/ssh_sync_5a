# RAID
Il termine **RAID** sta per *Redundant Array of Independent Disks*. In parole povere, è una tecnologia che permette di raggruppare più hard disk o SSD in un'unica unità logica.

Perché lo si fa? Principalmente per due motivi: **sicurezza dei dati** (ridondanza) e **velocità** (performance). A seconda di come "incastriamo" questi dischi, otteniamo diversi "livelli" di RAID.

Ecco una panoramica dei tipi più comuni utilizzati nelle reti aziendali e domestiche (NAS).

---

## 1. RAID 0: Lo scattista (Striping)
Nel RAID 0, i dati vengono frazionati e scritti contemporaneamente su due o più dischi. È il massimo per la velocità, ma il peggiore per la sicurezza.

* **Vantaggio:** Velocità di lettura e scrittura elevatissima.
* **Svantaggio:** **Nessuna tolleranza ai guasti.** Se un solo disco si rompe, perdi tutto il contenuto dell'intero array.
* **Uso tipico:** Editing video temporaneo o file di swap dove la perdita dati non è critica.



---

## 2. RAID 1: Il prudente (Mirroring)
Qui i dati vengono duplicati esattamente su due dischi. Tutto quello che scrivi sul disco A viene scritto identico sul disco B.

* **Vantaggio:** Massima sicurezza. Se un disco muore, l'altro continua a funzionare senza interruzioni.
* **Svantaggio:** Costoso. Paghi per due dischi ma hai lo spazio di uno solo (efficienza del 50%).
* **Uso tipico:** Server critici, database di piccole dimensioni, sistemi operativi.



---

## 3. RAID 5: L'equilibrato (Parity)
È il re dei sistemi NAS e dei server di rete. Richiede almeno **3 dischi**. I dati vengono distribuiti su tutti i dischi insieme a delle informazioni di "parità".

* **Vantaggio:** Ottimo compromesso tra velocità, capacità e sicurezza. Può "sopravvivere" alla rottura di **un disco** senza perdere dati.
* **Svantaggio:** Se si rompe un secondo disco prima di aver sostituito il primo, i dati sono persi. La ricostruzione di un disco rotto può essere lenta.
* **Uso tipico:** File server aziendali, storage condiviso.



---

## 4. RAID 6: Il corazzato (Double Parity)
Evoluzione del RAID 5, richiede almeno **4 dischi**. Utilizza una doppia parità distribuita.

* **Vantaggio:** Può sopportare il guasto simultaneo di **due dischi**. Estremamente affidabile per array molto grandi.
* **Svantaggio:** Più lento in scrittura rispetto al RAID 5 a causa del calcolo della doppia parità.
* **Uso tipico:** Grandi archivi dati (Big Data) e sistemi dove l'affidabilità è l'unica priorità.

---

## 5. RAID 10 (1+0): L'atleta d'élite
È una combinazione (annidata): unisce il Mirroring (RAID 1) e lo Striping (RAID 0). Richiede almeno **4 dischi**.

* **Vantaggio:** Il meglio dei due mondi. Velocità del RAID 0 e sicurezza del RAID 1. Molto performante con i database pesanti.
* **Svantaggio:** Molto costoso (perdi il 50% della capacità totale per la ridondanza).
* **Uso tipico:** Server ad alte prestazioni, database SQL, ambienti virtualizzati intensivi.



---

### Tabella Comparativa Rapida

| Livello RAID | Min. Dischi | Tolleranza Guasti | Velocità | Efficienza Spazio |
| :--- | :--- | :--- | :--- | :--- |
| **RAID 0** | 2 | 0 dischi | Eccellente | 100% |
| **RAID 1** | 2 | 1 disco | Buona (lettura) | 50% |
| **RAID 5** | 3 | 1 disco | Molto buona | $n-1$ dischi |
| **RAID 6** | 4 | 2 dischi | Buona | $n-2$ dischi |
| **RAID 10** | 4 | Almeno 1 per mirror | Eccellente | 50% |

**Nota bene:** Il RAID **non è un backup**. Protegge dalla rottura hardware del disco, ma non da virus, cancellazioni accidentali o incendi. Un backup esterno rimane sempre necessario!

Vorresti che ti aiutassi a calcolare lo spazio effettivo disponibile per una specifica configurazione di dischi che hai in mente?