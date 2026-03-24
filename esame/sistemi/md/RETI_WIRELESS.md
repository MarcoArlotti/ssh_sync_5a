# RETI WIRELESS
Ecco una panoramica strutturata sulle reti wireless, organizzata per essere salvata direttamente in un file `.md` (Markdown).

---

# Le Reti Wireless: Architettura e Tipologie

Le reti wireless (senza fili) rappresentano il sistema di comunicazione che permette lo scambio di dati tra dispositivi tramite onde elettromagnetiche, eliminando la necessità di cavi fisici. Questa tecnologia si basa sullo spettro delle radiofrequenze (RF) o, in alcuni casi, sull'infrarosso.

## 1. Funzionamento Generale
Le reti wireless operano convertendo i dati digitali in segnali radio. Questi segnali vengono trasmessi da un'antenna, viaggiano attraverso l'aria e vengono ricevuti da un'altra antenna che li riconverte in dati digitali.



---

## 2. Classificazione per Estensione (Copertura)
Le reti wireless vengono classificate principalmente in base alla loro portata geografica, seguendo uno schema simile a quello delle reti cablate.

### WPAN (Wireless Personal Area Network)
Reti a brevissimo raggio, solitamente limitate a pochi metri (1-10m). Sono utilizzate per connettere dispositivi personali.
* **Esempi:** Bluetooth (per cuffie, mouse), Zigbee (per domotica), NFC.

### WLAN (Wireless Local Area Network)
Coprono un'area limitata come una casa, un ufficio o un intero edificio. È la tipologia più diffusa nel quotidiano.
* **Tecnologia dominante:** **Wi-Fi** (basato sullo standard IEEE 802.11).

### WMAN (Wireless Metropolitan Area Network)
Progettate per coprire aree urbane o interi campus universitari, connettendo più edifici tra loro.
* **Esempio:** WiMAX.

### WWAN (Wireless Wide Area Network)
Coprono aree geografiche vastissime (nazioni o continenti) sfruttando i ponti radio e i satelliti.
* **Esempi:** Reti cellulari (4G LTE, 5G) e comunicazioni satellitari.

---

## 3. Principali Tecnologie e Standard

| Tipo | Standard | Frequenze Tipiche | Utilizzo Principale |
| :--- | :--- | :--- | :--- |
| **Wi-Fi** | IEEE 802.11 | 2.4 GHz, 5 GHz, 6 GHz | Accesso Internet locale |
| **Bluetooth** | IEEE 802.15.1 | 2.4 GHz | Periferiche e audio |
| **5G** | 3GPP | Varie (Sub-6 GHz, mmWave) | Mobile e IoT massivo |
| **LoRaWAN** | LoRa | Sub-GHz (es. 868 MHz) | Sensori a lungo raggio e basso consumo |

---

## 4. Vantaggi e Svantaggi

### Vantaggi
* **Mobilità:** Gli utenti possono connettersi spostandosi liberamente nell'area di copertura.
* **Flessibilità:** Facilità di installazione in edifici storici o dove non è possibile passare cavi.
* **Scalabilità:** È facile aggiungere nuovi dispositivi senza dover modificare l'infrastruttura fisica.

### Svantaggi
* **Sicurezza:** I segnali radio possono essere intercettati più facilmente rispetto ai cavi (richiedono crittografia forte come WPA3).
* **Interferenze:** Altri dispositivi elettronici o ostacoli fisici (muri in cemento, metalli) possono degradare il segnale.
* **Velocità:** Generalmente inferiore rispetto alle connessioni cablate (come la fibra ottica o l'Ethernet Gigabit).

---

## 5. Topologie di Rete
Le reti wireless possono essere strutturate in due modi principali:
1.  **Modalità Infrastruttura:** I dispositivi comunicano tramite un punto centrale chiamato **Access Point (AP)**.
2.  **Modalità Ad-Hoc / Mesh:** I dispositivi comunicano direttamente tra loro, creando una rete magliata dinamica.



---

**Ti serve approfondire una tecnologia specifica, come ad esempio il funzionamento del protocollo WPA3 per la sicurezza?**