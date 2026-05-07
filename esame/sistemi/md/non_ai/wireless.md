# 1.1 Le reti Wireless
Il piu' grande vantaggio di un arete wireless e' nella facilita' con cui si possono estendere le reti aziendali, eliminando i costi dovuti a cablaggio e non avendo piu' la necessita' di usare postazioni fisse.

Tanto ormai la maggior parte dei produttori integra nei dispositivi, schede di rete wireless e con antenna.

La dimensione della rete wireless e' classiicata in:

## 1.2 WPAN
Le WPAN coprono una distanza di 10-15 metri,
sono adatte a reti domestiche.

La domotica fa parte delle reti WPAN.

### Bluetooth 802.15
La maggior parte delle WPAN vengono realizzate tramite il protocollo BLUETOOTH che usa onde radio per trasferire informazioni.

Per usare le onde radio bisogna rispettare le frequenze libere dell' ISM (frequenze radio assegnati per scopi industriali, scientifici e medici).

La frequenza usata dal bluetooth e' la 2.4 Ghz con una velocita' stimata di 2Mbps.

#### ALTRE VERSIONI DEL BLUETOOTH

Con il BLUETOOTH 5.0 si copre una distanza di 240 metri.
Mentreco con il BLUETOOTH Low Energy si garantisce un risparmio di energia cosumata.

### La PICONET
Bluetooth e' adatto a gestire piccole reti (max 8 dispositivi accesi) di corto raggio e a basso consumo.

Chi avvia una connessione e' detto MASTER e i dispositivi connessi a lui sono detti SLAVE.

I dispositivi che vogliono collegarsi alla PICONET ascoltano adintervalli di 2 secondi,
Il MASTER accetta la richiesta nel giro un secondo.

Quando si vuole collegare un nuovo dispositivo si dice fase di PAIRING che avviene dopo aver di solito premuto un pulsante, successivamente la connessione va accettata inserendo un PIN che lo SLAVE fornisce.
Una volta collegato il dispositivo nuovo viene messo in una lista dei dispositivi della PICONET per auto collegarsi in automatico le successive volte.

### SCATTERNET
Uno SLAVE puo' partecipare a piu' PICONET allo stesso tempo detta SCATTERNET.
I dispositivi dentro alla scatternet possono comunicare con tutti i dispositivi.

### IrDA
IrDA usa infrarossi per creare un collegamento, e' utile in situazioni di forte interferenze di onde radio, ma il segnale viene interrotto dagli oggetti fisici che passano in mezzo al flusso di dati (1-2 metri di raggio).

## 1.3 WLAN IEEE 802.11
Le Wireless LAN sono molto simili di prestazione rispetto alle LAN cablate.

Ma a contrario delle LAN cablate, le WLAN sono molto facili da espandere.

Le reti WLAN sono composte da:
- WT (Wireless Terminal): che sono i dispositivi host.
- AP (Access Point): possono essere usati come BRIDGE per collegare la rete cablata con quella wireless,
    e permette ai WT di collegarsi alla WLAN.

L'insieme di AP e delle stazioni e' detto BSS (Basic Service Set) che costituisce una CELLA, ogni CELLA ha un BSS-ID come identificativo che corrisponde al MAC del punto di accesso.

E' possibile collegare piu' AP tra loro creando un WDS (Wireless Distribution System).

Due o piu' WDS formano un ESS (Extend Service Set) che fa apparire la rete in una unica WLAN.

Un ESS puo' essere composto da:
- BSS parzialmente sovrapposto: (permette una copertura continua)
- BSS fisicamnete congiunti: ()
- BSS co-locati: (sono diversi BSS nella stessa area per ottenere rindondanza e migliori velocita')

Lo sposamento dei dipositivi viene gstita con:
- transizione statica: (il WT si sposta solo tra gli AP)
- transizione tra BSS: (il WT si sposta tra in altri BSS)
- transizione tra ESS: (il WT si sposta tra in altri BSS diversi, quindi perde il suo ip assegnato)

Nelle WLAN domestiche l'AP funge sia da router che da switch, con anche funzionalita' di FIREWALL.

### Da cosa e' composto un AP

#### 1. SSID
E' il nome della WLAN, che viene condiviso in broadcast con i WT in continuazione (BEACON).

Puo' capitare che piu' AP abbiano o stesso SSID, in piu' un AP puo' avere piu' SSID,
oppure direttamente il SSID puo' non essere inviato in broadcast creando una rete nascosta.

#### 2. Potenza
ETSI impone di non poter superare i 100mW di EIRP (potenza isotropica effettivamente irradiata).
Gli AP usano o la 2.4GHz oppure la 5GHz.

#### 3. Canale
Per evitare interferenze tra AP si applica la regola del 5, cioe' si tengono gli AP su canali ognuno distante dall'altro di 5 canali.

#### 4. Crittografia
Di base le WLAN offrono la WEP (Wired Equivalent Privacy) che usa una crittografia simmetrica che vale solo per la parte WLAN di tutta la rete.

#### 5. incapsulamento
Se l'AP e' anche un router dovra incapsulare i pacchetti che usciranno dalla rete.
I piu' comuni sono:
- PPPoA
- PPPoE

Ora gli ISP sono messi in AUTOSENSE in modotale da capire che incampsulamento viene usato dal router.

#### 6. NAT
L'AP che fara' da router dovra' convertire l'ip privato dalla rete in uno pubblico.

#### 7. DHCP
L'AP che fara' da router dovra' offrire l'assegnazione automatica degli IP tramite DHCP.

### RETI AD HOC
in situazioni dove non si puo' mettere un AP, si crea una rete MANET (Mobile ad hoc NETwork).
I WT comunicano direttamente tra loro con IBSS (Indipendent Basic Service Set).

La rete ad hoc funziona similmente come una rete PEER-TO-PEER.

## WMAN