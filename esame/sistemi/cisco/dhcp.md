Configurare il DHCP (Dynamic Host Configuration Protocol) su un router Cisco in Packet Tracer è un ottimo modo per automatizzare l'assegnazione degli indirizzi IP nella tua rete. Esistono due modi principali per farlo: configurare un **Router** come server DHCP o utilizzare un **Server dedicato**.

Ecco la guida passo-passo per la configurazione tramite **Router**, che è il metodo più comune.

---

## 1. Topologia di Base
Per questo esempio, immagina di avere:
* Un **Router** (es. modello 2911).
* Uno **Switch**.
* Due o tre **PC**.
* Cavi Ethernet che collegano tutto.

---

## 2. Configurazione dell'interfaccia del Router
Prima di attivare il DHCP, l'interfaccia del router collegata alla LAN deve avere un indirizzo IP statico (sarà il *Default Gateway* dei tuoi PC).

1.  Clicca sul Router e vai nella scheda **CLI**.
2.  Digita i seguenti comandi:

```bash
Router> enable
Router# configure terminal
Router(config)# interface gigabitEthernet 0/0  (o la porta che stai usando)
Router(config-if)# ip address 192.168.1.1 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# exit
```

---

## 3. Configurazione del Pool DHCP
Ora creiamo il "pool", ovvero l'intervallo di indirizzi che il router distribuirà.



### Escludere indirizzi (Opzionale ma consigliato)
È bene escludere i primi indirizzi (usati per router o stampanti) per evitare conflitti:
```bash
Router(config)# ip dhcp excluded-address 192.168.1.1 192.168.1.10
```

### Creare il Pool
```bash
Router(config)# ip dhcp pool MIO_POOL
Router(dhcp-config)# network 192.168.1.0 255.255.255.0
Router(dhcp-config)# default-router 192.168.1.1
Router(dhcp-config)# dns-server 8.8.8.8
Router(dhcp-config)# exit
```

---

## 4. Verifica sui PC
Dopo aver configurato il router, devi dire ai PC di smettere di aspettare un IP statico e chiederne uno al server:

1.  Clicca su un **PC**.
2.  Vai nella scheda **Desktop** > **IP Configuration**.
3.  Seleziona l'opzione **DHCP**.
4.  Dovresti vedere apparire il messaggio *"DHCP request successful"* e i campi IP, Subnet e Gateway compilarsi automaticamente.

---

## Tabella dei Comandi Principali

| Comando | Descrizione |
| :--- | :--- |
| `ip dhcp pool [NOME]` | Crea il pool e accede alla modalità configurazione DHCP. |
| `network [RETE] [SUBNET]` | Definisce il range di indirizzi disponibili. |
| `default-router [IP]` | Imposta il gateway predefinito per i client. |
| `ip dhcp excluded-address` | Impedisce al router di assegnare specifici IP. |
| `show ip dhcp binding` | Visualizza quali IP sono stati assegnati e a quali dispositivi. |

---

> **Nota:** Se vuoi usare un **Server fisico** (l'icona "Server" in Packet Tracer), la procedura è ancora più semplice: basta andare nella scheda **Services** del server, selezionare **DHCP**, impostare i parametri nella tabella e cliccare su **On**.