# i rischi delle reti WIRELESS
Ecco una panoramica strutturata sui rischi delle reti wireless e le best practice per la loro messa in sicurezza in un contesto enterprise.

---

# Sicurezza delle Reti Wireless Aziendali: Rischi e Implementazione

L'adozione del Wi-Fi in azienda offre flessibilità e produttività, ma espone l'infrastruttura a vettori di attacco che non esistono nelle reti cablate. Poiché il segnale radio supera i confini fisici degli uffici, la difesa del perimetro diventa una sfida puramente logica e crittografica.

## 1. Principali Rischi delle Reti Wireless

I rischi associati al Wi-Fi possono essere classificati in base alla tipologia di minaccia:

* **Intercettazione dei dati (Eavesdropping):** Senza una crittografia robusta, i pacchetti trasmessi nell'aria possono essere catturati da chiunque si trovi nel raggio di portata del segnale.
* **Access Point Canaglia (Rogue AP):** Un dipendente potrebbe installare un router economico per comodità, creando un "buco" nella sicurezza aziendale non gestito dal reparto IT.
* **Attacchi Man-in-the-Middle (MitM):** Un attaccante può creare un SSID con lo stesso nome di quello aziendale (Evil Twin) per indurre i dispositivi a connettersi ad esso, intercettando così credenziali e traffico.
* **Denial of Service (DoS):** Attacchi di "deauthentication" possono disconnettere forzatamente gli utenti dalla rete, interrompendo l'operatività.
* **Accessi non autorizzati:** L'uso di password deboli o protocolli obsoleti (come WEP o WPA) permette agli attaccanti di entrare nella rete interna con relativa facilità.



---

## 2. Strategie di Implementazione Sicura

Per mitigare questi rischi, una rete aziendale deve abbandonare le configurazioni "domestiche" a favore di standard **Enterprise**.

### A. Protocolli di Cifratura e Autenticazione
* **WPA3-Enterprise:** È lo standard attuale più sicuro. A differenza del WPA3-Personal, utilizza l'autenticazione basata su server (802.1X), garantendo chiavi di cifratura uniche per ogni sessione utente.
* **Standard IEEE 802.1X:** Implementa un server **RADIUS** (Remote Authentication Dial-In User Service). Gli utenti non inseriscono una password condivisa, ma si autenticano con le proprie credenziali aziendali (Active Directory/LDAP) o certificati digitali.

### B. Segmentazione della Rete (VLAN)
Non tutti gli utenti hanno bisogno dello stesso livello di accesso. Una rete ben progettata deve prevedere almeno tre segmenti:
1.  **Corporate VLAN:** Accesso completo alle risorse critiche, protetta da 802.1X.
2.  **Guest VLAN:** Solo accesso a Internet, isolata dalla rete interna e soggetta a "Client Isolation" (i dispositivi ospiti non possono vedersi tra loro).
3.  **IoT VLAN:** Per stampanti, sensori o telecamere, spesso meno sicuri e quindi da isolare rigorosamente.

### C. Gestione degli Access Point e Monitoraggio
* **WIPS (Wireless Intrusion Prevention System):** Utilizzare controller che scansionano costantemente lo spettro radio per identificare e neutralizzare automaticamente Rogue AP o attacchi di jamming.
* **Controllo della potenza del segnale:** Regolare le antenne per minimizzare la fuoriuscita del segnale all'esterno dell'edificio aziendale.
* **Nascondere l'SSID?** (Nota: Questa è spesso considerata una misura di sicurezza, ma è puramente estetica; gli strumenti di hacking possono trovare SSID nascosti in pochi secondi).

---

## 3. Checklist per il Network Administrator

| Azione | Descrizione |
| :--- | :--- |
| **Certificati Digitali** | Preferire l'uso di certificati (EAP-TLS) rispetto alle password per l'autenticazione 802.1X. |
| **Disabilitare il WPS** | Il Wi-Fi Protected Setup è una vulnerabilità critica e va sempre disattivato. |
| **Update del Firmware** | Aggiornare costantemente AP e controller per patchare vulnerabilità note (es. KRACK o Dragonblood). |
| **VPN obbligatoria** | Imporre l'uso di una VPN aziendale per i dipendenti che si connettono da reti Wi-Fi pubbliche o domestiche. |

---

> **Nota Tecnica:** La sicurezza wireless non è un evento singolo, ma un processo continuo di monitoraggio. L'anello più debole rimane spesso l'utente: la formazione sul phishing e sulla scelta di credenziali robuste è fondamentale quanto la configurazione del firewall.

Desideri che approfondisca la configurazione tecnica di un server RADIUS o che crei uno schema di segmentazione VLAN specifico per la tua infrastruttura?