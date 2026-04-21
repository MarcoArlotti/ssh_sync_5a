# I vari tipi diversi di linguaggi di programmazione

Ogni linguaggio di programmazione ha una sua sintassi e regole da seguire
per avere un codice valido e funzionante, e' fondamentale mantenere corretta:
1. la semantica
2. la sintassi
3. l'intestazione (non in tutti i linguaggi)

## Linguaggio macchina e astratto
I linguagi compilati sono dei linguaggi che da un codice sorgente, che usa
uno sviluppatore per programmare, per poi esser eseguito dovra'
prima essere compilato dal compilatore, la compilazione consiste nel convertire
il codice del suddeddo linguaggio in linguaggio macchina composto da 0 e 1 che sara' diverso per ogni architettura e tipo di processore.

Il linguaggio macchina e' un linguaggio a Basso Livello (il meno astratto che ci sia),
piu' un linguaggio di programmazione e' astratto piu' avra' una sintassi
piu' complessa e ricca di opzioni da leggere per i programatori.

Mentre un Linguaggio ad Alto Livello (più astratto),
Si chiama così perché è più lontano dall'hardware, ma più vicino al linguaggio umano.
La sintassi è più semplice e intuitiva per l'uomo. Con una riga di codice puoi fare operazioni che richiederebbero centinaia di righe in linguaggio macchina.

Un linguaggio a basso livello tende ad essere molto vicino al linguaggio macchina,
cio' significa che l'interprete o il compilatore dovranno fare meno lavoro.

La sintassi è considerata più "difficile" o "ostica" perché si deve gestire manualmente la memoria e i registri del processore.

## linguaggio interpretato e compilato
Un liguaggio si dice compilato quando il su codice sorgente viene convertito
in linguaggio macchina, questo processo viene fatto tramite un analisi
automatica di tutto il codice automaticamnte dal compilatore.

Dei liguagi compilati sono:
- C
- C++
- C# (usa una versione ibrida)
- Rust

Come risultato da questo rpocesso si avra' un file eseguibile (.exe).

il liguaggio interpretato legge riga per riga il codice per vedere se e' valido, man mano che lo si esegue.
Dei liguagi interpretati sono:
- python (usa una versione ibrida)
- javaScript
- PHP
- Ruby

Il linguagio compilato ha il vantaggio che una volta che lo si ha compilato,
non lo si deve mai piu' ricompilarlo, quindi velocizzando la esecuzione.

Ma come lato negativo ha il problema che ad ogni nuova modifica del codice, tutto il codice dovrà essere di nuovo compilato da capo.

E in piu' il codice compilato non puo' essere usato da macchine diverse,
visto che ogni lignuaggio macchina verra' scritto diversamente per ogni
computer diverso.

## Linguggi di tipo FRONTEND
Nello sviluppo di una WEB APP
esistono linguaggi dedicati al Frontend (Client-Side), cioe' il codice dell'interfaccia utente (UI) che gira sul browser di un eventuale host che si connette ad un WEB SERVER,

>Linguaggi di MARKUP:
>- HTML: Definisce la struttura semantica della pagina.
>- CSS: Gestisce lo stile e grafica dell'interfaccia.
>- React.

>Linguaggi per la logica:
>- JavaScript: Rende interattive le pagine statiche, permettendo di modificare il contenuto della pagina in modo dinamico senza ricaricarla.


## Linguggi di tipo BACKEND
Il BACKEND invece e' il codice che viene eseguito dal server:
- Prendere i dati di un eventuale DATABASE collegato alla WEB APP, per inviarli all'utente, mostrando le informazioni ricevute dal DB attraverso la interfaccia grafica.
- Verifica l'autenticazione degli utenti e blocca l'invio di dati sensibili ai non autorizzati.
- Si occupa di fare calcoli matematico logici.
- Si occupa anche di collegarsi ad API che permette alla WEB app di collegarsi a delle altre web app esterne scambiandosi inforazioni.
- Archiviano dati e inforazioni all'interno di un DATABASE