# Il Concetto di Superset di C: C++ e Objective-C

Nel mondo della programmazione, un **Superset** (soprainsieme) è un linguaggio che include tutta la sintassi di un altro linguaggio (il sottoinsieme), aggiungendo però nuove funzionalità, librerie o paradigmi.

Poiché il C è un linguaggio procedurale "vicino all'hardware", i suoi superset sono stati creati principalmente per gestire la complessità dei grandi software attraverso la **Programmazione Orientata agli Oggetti (OOP)**.

---

## 1. C++: Il Superset più Diffuso

Creato da Bjarne Stroustrup nel 1979 (originariamente chiamato "C with Classes"), il C++ è il principale erede del C. 

### Caratteristiche Chiave
* **Compatibilità Retroattiva:** Quasi ogni programma scritto in C standard è un programma C++ valido.
* **Classi e Oggetti:** Introduce l'incapsulamento dei dati.
* **Ereditarietà e Polimorfismo:** Permette di creare gerarchie di codice riutilizzabile.
* **Template:** Consente la programmazione generica (scrivere codice che funziona con qualsiasi tipo di dato).

### Schema di Evoluzione


| Funzionalità | C (Sottoinsieme) | C++ (Superset) |
| :--- | :--- | :--- |
| **Paradigma** | Procedurale | Multiparadigma (Procedurale + OOP) |
| **Gestione Memoria** | Manuale (`malloc`, `free`) | Manuale + Automatica (`new`, `delete`, Smart Pointers) |
| **Standard Library** | `stdio.h`, `stdlib.h` | STL (Standard Template Library), `iostream`, `vector` |

---

## 2. Objective-C: Il Superset "Smalltalk-style"

Mentre il C++ aggiungeva classi in stile simula, l'Objective-C ha aggiunto al C un sistema di messaggistica ispirato al linguaggio Smalltalk. È stato il linguaggio base di Apple (macOS e iOS) prima dell'arrivo di Swift.

### Differenze Filosofiche
* **Runtime Dinamico:** Molte decisioni vengono prese durante l'esecuzione del programma, non durante la compilazione.
* **Sintassi dei Messaggi:** Utilizza le parentesi quadre per chiamare i metodi: `[oggetto metodo:parametro]`.

---

## 3. Perché usare un Superset invece del C puro?

Il C è imbattibile per performance e sistemi embedded, ma i suoi superset offrono:
1.  **Astrazione:** È più facile modellare concetti del mondo reale.
2.  **Sicurezza:** Gestione delle eccezioni e sistemi di tipi più severi.
3.  **Manutenibilità:** Gestire milioni di righe di codice in C puro è estremamente complesso; l'OOP aiuta a compartimentare il software.

---

## Esempio Pratico di Sintassi

Ecco come la stessa operazione evolve dal C al suo superset C++:

### In C (Procedurale)
```c
struct Rettangolo {
    float larghezza;
    float altezza;
};

float calcolaArea(struct Rettangolo r) {
    return r.larghezza * r.altezza;
}