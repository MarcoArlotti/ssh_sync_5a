L'Italia è uno dei maggiori produttori di vino al mondo; numerose denominazioni, vitigni autoctoni e tradizioni locali caratterizzano il territorio. Il progetto prevede la realizzazione di una banca dati per la raccolta, gestione e consultazione dei dati relativi alle **aziende vinicole** e alle produzioni dei loro vigneti.

Per consentire una modellazione coerente sono state individuate le seguenti informazioni e vincoli:

- Le **aziende vinicole** __sono identificate da una partita IVA__ (o codice fiscale) e hanno: __nome__, __via__, __numero civico__, __comune__, __provincia__ e __regione__.

- Ogni **azienda** "può possedere più" **vigneti**. Un vigneto è individuato da un __codice univoco__ e annotato con: __nome__, __superficie totale__ (ettari), __località__, __comune__, __classe di esposizione__ (es: "nord", "sud", "est", "ovest") e __numero di filari__.

- Ogni **vigneto** "è suddiviso" ''in uno o più'' **blocchi** (parcelle), ciascuno con un __codice__ identificativo, __superficie__ (ettari), e __classe di esposizione__. Questa suddivisione permette di rappresentare variazioni locali all'interno dello stesso vigneto.

- I **vitigni** sono caratterizzati da __nome scientifico__, __nome__ __comune__, __colore__ della bacca ("rossa" o "bianca") e __origine genetica__.

- I vitigni sono piantati a livello di blocco: per ogni **blocco** si __specifica quali vitigni vi sono coltivati__ e, per ciascuno, __la percentuale della superficie del blocco occupata dal vitigno__. Questa struttura permette composizioni diverse tra blocchi dello stesso vigneto.

- Le **etichette** di vino rappresentano l'unità di produzione commerciale: ogni etichetta ha __nome__, __annata__ e __tipologia__ (es: "DOC", "IGT", "Vino da Tavola")._'' Un'etichetta è prodotta da un'azienda''_, _''proviene da un vigneto principale''_ e può essere associata a un vitigno prevalente.

Si richiede di modellare il dominio mediante un diagramma ER in cui siano chiaramente rappresentate entità, attributi (con chiavi primarie e chiavi esterne), relazioni e cardinalità.
