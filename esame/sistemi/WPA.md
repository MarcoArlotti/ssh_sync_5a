# WPA
Le reti wireless sono ormai il cuore pulsante della nostra connettività quotidiana. Capire come funzionano non è solo affascinante dal punto di vista tecnico, ma è il primo passo fondamentale per proteggere i propri dati.

Ecco un'analisi di come operano e di come il protocollo WPA agisca da "guardiano" del segnale.

---

## 1. Come funzionano le reti Wireless (Wi-Fi)

A differenza delle reti cablate, che trasmettono dati sotto forma di impulsi elettrici o luminosi attraverso i cavi, le reti wireless utilizzano **onde radio**. Il processo segue generalmente questa logica:

* **Conversione dei dati:** Quando invii un'informazione, il tuo dispositivo (PC, smartphone) traduce i dati digitali (0 e 1) in segnali radio.
* **Trasmissione:** Questi segnali vengono emessi tramite un'antenna su frequenze specifiche, solitamente **2.4 GHz** o **5 GHz**.
* **Ricezione e instradamento:** Il router wireless riceve queste onde, le decodifica nuovamente in dati digitali e le invia a internet tramite la connessione fisica (fibra o ADSL).

Il limite intrinseco? Poiché le onde radio si propagano in tutte le direzioni, **chiunque si trovi nel raggio d'azione può "ascoltare" il segnale**. È qui che entra in gioco la sicurezza.

---

## 2. Il ruolo del WPA (Wi-Fi Protected Access)

Senza crittografia, una rete Wi-Fi è come una conversazione urlata in una piazza affollata. Il protocollo **WPA** serve a "chiudere la porta", trasformando i dati leggibili in un codice cifrato che solo il mittente e il destinatario autorizzato possono comprendere.

### Evoluzione del WPA
Esistono tre versioni principali, ognuna più sicura della precedente:

1.  **WPA (2003):** Introdotto per risolvere le gravi falle del vecchio WEP. Utilizzava il protocollo TKIP per cambiare dinamicamente le chiavi di crittografia.
2.  **WPA2 (2004):** Lo standard attuale più diffuso. Utilizza l'algoritmo **AES** (Advanced Encryption Standard), lo stesso livello di sicurezza usato da governi e banche.
3.  **WPA3 (2018):** L'ultima frontiera. Protegge contro gli attacchi a "forza bruta" (tentativi ripetuti di indovinare la password) e rende più sicure le reti pubbliche.

---

## 3. Come rendere sicura la rete con WPA

Per implementare correttamente la sicurezza WPA nella tua rete, non basta "attivarla", ma occorre seguire alcune buone pratiche configurando il router:

### Scegliere la modalità corretta
Nella pagina di configurazione del router (solitamente accessibile via browser all'indirizzo `192.168.1.1`), troverai diverse opzioni. La gerarchia di sicurezza è la seguente:

| Protocollo | Livello di Sicurezza | Consiglio |
| :--- | :--- | :--- |
| **WEP** | Nullo | Da evitare assolutamente (si viola in pochi secondi). |
| **WPA-TKIP** | Basso | Superato, può rallentare la connessione. |
| **WPA2-AES (CCMP)** | **Ottimo** | Lo standard consigliato per compatibilità e forza. |
| **WPA3** | **Massimo** | Da usare se tutti i tuoi dispositivi sono recenti. |

### Configurazione della Password (PSK)
WPA utilizza spesso una "Pre-Shared Key" (PSK). Per renderla efficace:
* **Lunghezza:** Almeno 12-16 caratteri.
* **Complessità:** Mix di maiuscole, minuscole, numeri e simboli.
* **Unicità:** Non usare parole del dizionario o date di nascita.

### Disabilitare il WPS (Wi-Fi Protected Setup)
Il WPS è quel tastino che permette di connettersi senza password. Sebbene comodo, rappresenta un punto debole critico perché il suo PIN a 8 cifre può essere forzato facilmente. **Disabilitarlo è un passo fondamentale per una rete davvero sicura.**

---

### Conclusione
Il Wi-Fi trasmette i nostri segreti nell'aria; il WPA si assicura che nessuno possa leggerli. Passare a WPA2 o WPA3 e scegliere una password robusta sono le difese più efficaci contro le intrusioni.

**Ti piacerebbe che ti guidassi passo dopo passo nella configurazione dei parametri di sicurezza nel pannello di controllo del tuo specifico modello di router?**