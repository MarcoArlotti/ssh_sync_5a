# LE VPN
Le VPN nascono per collegare piu' aziende o singoli dipendenti alla rete privata di una sede principale di una azienda proprio come se fossero collegati fisicamente alla rete.

>aprendo le porte allo SMART WORKING, cioe' un dipendente che lavore da remoto.

La parte piu' importante di una VPN e' la sicurezza,
per collegare insieme le sedi al posto che piazzare un cavo fisico, molto costoso e che rischia danneggiamenti, si crea un collegamento logico tramite la rete pubblica come mezzo, ma introducono problemi come la ridotta lentezza e costi della banda usata.

Nel fare passare i pacchetti nella rete pubblica, e' fondamentale:
- applicare una cifratura,
- controllo degli accessi (autenticazione),
- tunneling dei pacchetti.

---

## Le varie classificazioni
Esistono 2 tipi principali di VPN:

## 1. REMOTE-ACCESS VPN
>Ha la funzione principale di desktop remoto per collegarsi alla LAN della sede principale,
>E' soprattutto usata per collegare piccole sedi o pochi dipendenti alla LAN principale.

I singoli utenti si collegano ad un server di accesso detto NAS
> NAS (NETWORK ACCESS SERVER)  che puo' essere dell'HARWARE dedicato o una semplice applicazione eseguita in un server condiviso.
>
>Il NAS chiede le credenziali all'utente, che se valide, gli permettera' di usare la VPN.

Il *NAS* per verificare la autenticazione puo' appoggiarsi ad un `RADIUS AAA SERVER` che lo fa al posto suo.
***AAA*** sta per:
- `Authentication` (verifica gli accessi),
- `Authorization` (verifica cio' che e' permesso),
- `Accounting` (tiene tracci adi chi fa che cosa {non ripiudabilita'}).

In piu' per funzionare, il client dovra' munirsi di un software VPN client.

>l'affitto di un NAS e' detto ESP,
>L'ESP configura il NAS e lo mantiene funzionante a chi lo affittera'.

## 2. SITE-TO-SITE VPN
>Si usa principalmente per collegare 2 sedi grosse insieme permettendogli di condividere le risorse (stampanti, pc, archivio).

Le VPN site to site eliminano la necessita' di avere una applicazione client VPN per ogni CLIENT.

La SITE-TO-SITE VPN si divide principalmente in:
- INTRANET BASED:
    >Una rete intranet collega 2 sedi in una unica.
- EXTRANET BASED:
    >Se l'azienda ha un rapporto stretto con un altra azienda esterna, EXTRANET permette di lavorare insieme in modo sicuro condividendo le risorse, senza dando l'accesso  preventivo e completo a tutto.

---

## La sicurezza delle VPN
Come mezzo le VPN usano la rete pubblica e' neccessario che il traffico venga crittografato.

Passando per una rete pubblica, i pacchetti devono mantenere la propria integrita' e autenticita'.

Il passi che una VPN deve seguire sono:

### 1. Autenticazione degli utenti (autenticazione)
Le VPN possono essere usati solo da determinati utenti,
quindi bisogna verificarnr la corretta identita' per l'accesso ad essa con un autenticazione.

Cio lo si fa tramite server NAS con un processo di autenticazione, o uno dedicato come l'AAA.

L'autenticazione ad una VPN sfrutta una MFA (Multy Factor Authentication),
che aggiunge un livello in piu' di sicurezza,

>In passato si usava che l'utente scriva un codice generato tramite una chiave elettronica (KEY FOB) che cambiava ogni volta.
>
>Ma ora si utilizzano applicazioni da smartphone che generano un OTP (One Time Password) che genera una sequenza di caratteri casuali da inserire, o direttamente l'impronta di un dito (Fingerprint), o un QR code.

Solo dopo aver eseguito l'autenticazione, all'utente viene concessa l'autorizzazzione per usare i servizi della rete.

Grazie all'autenticazione si possono apportare misure di accounting per salvarsi i vari accessi e la quantita' di dati in entrata e uscita,
tempi di utilizzo dei vari utenti (durata di sessione per tariffare l'utilizzo della rete) e quali risorse si hanno usato attraverso dei file di log.

---

## 2. Cifratura dei dati (CRITTOGRAFIA)

Le VPN utilizzano il protocollo IKE (Internet Key Exchange), che ha lo scopo di automatizzare lo scambio delle chiavi.

I principali protocolli che applicano la crittografia sono:
- IPsec (IP security),
- SSL/TLS (Secure Socket layer / Trasport Layer Security),
- BGP/MPLS (Border Gateway Protocol / Multiprotocol Lable Switching).

## 3. TUNNEL o MODALITA' TRASPORTO
### Trasporto
In modalita' trasporto, e' compito del software a collegarsi alla VPN e soprattutto questo approccio rende compatibile la VPN con qualunque ISP della rete,
in quanto cifratura e decifratura verra' gestita dal software,
Lasciando in chiaro solamente le informazioni per instradare il pacchetto.

### Tunnel
Invece con il TUNNELING si utilizzano gli apparati di rete, in particolare i FIREWALL e ROUTER, questo approccio nasconde all'utente la presenza di una VPN, in questa modalita' gli apparati di rete apposta modificano il traffico della VPN incapsulandolo in un pacchetto, proteggiendo cosi' il pacchetto originale proteggendolo completamente, mostrando cosi' solo quello esterno.

I dispositivi che fanno questo compito sono detti tunnel interface.

1. IPV6 fa da PASSENGER PROTOCOL,
2. IPsec fa da TUNNELING PROTOCOL,
3. IPV4 fa da CARRIER PROTOCOL.

I due router in entrata delle LAN deve essere di tipo DUAL STACK in modo da poter comprendere sia IPV6 che IPV4.

## - IPsec
IPsec non e' solo un protocollo ma e' una vera e propria architettura di sicurezza del livello NETWORK,
i 3 principali protocolli che la compongono sono:

- AH (Authentication Header):
    >che garantisce solo la AUTENTICAZIONE e la INTEGRITA' ma ***NON*** cifra il transito.
- ESP (Encapsulating Security Payload):
    > che comprende anche la CIFRATURA dei messaggi
- IKE (Internet Key Exchange):
    > si occupa di gestire e scambiare le chiavi per la crittografia della comunicazione, e lavora al livello APPLICATION.

Sia AH che ESP possono essere usati o in modalita' TRASPORTO o in TUNNEL, di cui per essere usati hanno bisogno di creare una connessione LOGICA detta SA (Security association) lavora al livello NETWORK e viene fatta grazie all'IKE.

IKE usa UDP per comunicare pero' usa un servizio affidabile, in caso la richiesta di connessione non arriva IKE ritrasmettera' la richiesta.

Una connessione con SA dura poco e fa trasmettere pochi dati, in caso che serva inviare piu' dati,
si instaura una nuova SA.

IPsec usa due SECURITY GATEWAY alle entrate delle LAN per incapsulare o leggere il pacchetto, che sara' in arrivo o in uscita.

In questo modo il pacchetto da inviare usera' il suo routing, mentre il pacchetto che lo INCAPSULA usa il routing per spedirlo alla LAN.

Le SA sono UNIDIREZIONALI, quindi si dovranno creare 2 SA in caso si voglia comunicare da entrambi i lati.

Tutte le SA sono salvate all'interno di un SAD (Security Association Database), mentre le politiche di sicurezza (quali ip scartare) vengono salvate nel SPD (Security Policy Database).

### 1. Traffico in Uscita (Outbound)
*Outbound segue le fasi:*
1. ***Il Controllo SPD***:
Quando un pacchetto deve uscire, il sistema consulta l'SPD, che puo' causare tre esiti possibili:

    1. Il pacchetto viene scartato (firewall).

    2. Il pacchetto passa senza IPsec (traffico in chiaro).

    3. Il pacchetto deve essere protetto da IPsec.

2. ***Associazione al SAD***:
Se l'esito è il (3), si cerca nel SAD (Security Association Database) se esiste già una SA (una "connessione sicura") attiva per quel tipo di traffico.

    1. Se esiste: Si usa la chiave e l'algoritmo già pronti.

    2. Se NON esiste: Si avvia il protocollo IKE (Internet Key Exchange) per negoziare le chiavi in tempo reale, creare la SA e registrarla nel SAD.

3. ***Fase di Trasformazione***:
Solo a questo punto il pacchetto viene processato (Cifratura/Autenticazione) e incapsulato.

### Traffico in ingresso (inbound)

In ingresso il processo è "inverso", ma con un controllo di sicurezza fondamentale alla fine:

1. ***Riassemblaggio***:
Corretto. Se il pacchetto è frammentato, va ricomposto prima di poter leggere gli header IPsec.

2. ***Identificazione***:
Il ricevente vede che il protocollo nell'header IP non è TCP o UDP, ma ESP (50) o AH (51).

3. ***Lookup tramite SPI***:
Qui c'è un dettaglio importante. Per trovare la SA giusta nel SAD, il ricevente usa una "tripletta" di valori:

    1. SPI (Security Parameters Index) – che si trova nell'header ESP/AH.

    2. Indirizzo IP Destinazione.

    3. Protocollo di sicurezza (AH o ESP).

4. ***Decapsulamento***:
Una volta trovata la SA, il pacchetto viene decifrato e autenticato.

5. ***Il controllo finale dell'SPD (Fondamentale)***:
Questo è il punto che spesso sfugge. Dopo aver "estratto" il pacchetto originale, il sistema ricontrolla l'SPD. Perché? Per verificare che quel pacchetto sia effettivamente arrivato con la protezione corretta.

## - AH, ESP, IKE nel dettaglio

### 1. AH (Authentication Header)
AH fornisce:
- autenticazione,
- integrita'

>contro gli attacchi di tipo replay, in cui un malintenzionato mette in rete un pacchetto clonato precedentemente intercettandolo.

AH autentica l'intero pacchetto IP ad eccezzione dei campi variabili dell'header IP originale.

AH aggiunge il campo SPI (Security Parameters Index) che contiene un valore numerico che insieme con l'IP di destinazione e il protocollo AH identifica la SA usata.

In modalita' tunnel l'intero pacchetto e' incapsulato in un nuovo pacchetto autenticandolo tutto nel processo.

### 2. ESP (Encapsulating Security Payload)

ESP aggiunge la crittografia che manca ad AH.

A contrario di AH, ESP non authentica tutto il pacchetto, non coprendo l'header IP:
> 1. in trasporto l'header ip originale e' in chiaro.

> 2. in tunnel l'header originale viene cifrato ma quello esterno no.

ESP all'interno del pacchetto aggiunge:
- HEADER ESP (per incapsulare)
- TRAILER ESP (per incapsulare)
- AUTHENTICATION ESP (per autenticare)

Simile ad AH, nell'header ESP  e' presente il campo SPI che identifica la SA usata per quel pacchetto.

### 3. IKE (Internet Key Exchange)
Le SA possono essere fatte manualmente, ma non e' fisicamente fattible, come soluzione si usa IKE.
IKE si occupa di creare delle nuove SA ogni volta che serva.

IKE realizza un collegamento peer-to-peer in due fasi:
    1. fase 1:
        I 2 host creano una nuova SA per IKE stesso (IKE SA), che verra' usata per creare nuove SA in modo sicuro.
    2. fase 2:
        Si usa la IKE SA creata per negoziare le altre SA da usare per gli altri protocolli.