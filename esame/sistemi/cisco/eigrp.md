Configurare EIGRP (**Enhanced Interior Gateway Routing Protocol**) su Cisco Packet Tracer è un'operazione piuttosto lineare, ma richiede precisione nella gestione degli indirizzi IP e delle maschere di sottorete (wildcard mask).

Ecco la guida passo-passo per configurare una rete EIGRP tra due o più router.

---

## 1. Topologia di Base
Immaginiamo una rete semplice:
* **Router A (R1):** Collegato alla sottorete `192.168.1.0/24`.
* **Router B (R2):** Collegato alla sottorete `192.168.2.0/24`.
* **Connessione tra i Router:** Una rete seriale o Ethernet sulla subnet `10.0.0.0/30`.

---

## 2. Configurazione degli Indirizzi IP
Prima di attivare il protocollo di routing, assicurati che le interfacce siano attive.

**Su Router R1:**
```bash
Router> enable
Router# configure terminal
Router(config)# interface gigabitEthernet 0/0
Router(config-if)# ip address 192.168.1.1 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# exit
Router(config)# interface gigabitEthernet 0/1
Router(config-if)# ip address 10.0.0.1 255.255.255.252
Router(config-if)# no shutdown
```

---

## 3. Configurazione EIGRP
Il comando fondamentale è `router eigrp [AS-NUMBER]`. Il numero del Sistema Autonomo (AS) deve essere lo **stesso** su tutti i router che devono comunicare.

### Passaggi su R1:
```bash
Router(config)# router eigrp 10
Router(config-router)# network 192.168.1.0 0.0.0.255
Router(config-router)# network 10.0.0.0 0.0.0.3
Router(config-router)# no auto-summary
```

### Passaggi su R2:
```bash
Router(config)# router eigrp 10
Router(config-router)# network 192.168.2.0 0.0.0.255
Router(config-router)# network 10.0.0.0 0.0.0.3
Router(config-router)# no auto-summary
```

> **Nota sulla Wildcard Mask:** In EIGRP si usa la maschera inversa. Per una `/24` (255.255.255.0) la wildcard è `0.0.0.255`. Per una `/30` (255.255.255.252) è `0.0.0.3`.

---

## 4. Comandi Chiave Spiegati

| Comando | Descrizione |
| :--- | :--- |
| `router eigrp 10` | Attiva il processo EIGRP con ID di sistema 10. |
| `network [rete] [wildcard]` | Indica al router quali interfacce includere nel processo EIGRP. |
| `no auto-summary` | Impedisce al router di riassumere automaticamente le rotte ai confini della rete (fondamentale per reti moderne). |
| `passive-interface [int]` | Impedisce l'invio di pacchetti EIGRP su interfacce dove ci sono solo PC (migliora la sicurezza). |

---

## 5. Verifica del Funzionamento
Una volta configurati entrambi i router, dovresti vedere un messaggio in console che indica che è stata stabilita un'**adiacenza** (Neighbor Adjacency).

Per verificare manualmente, usa questi comandi in modalità **Privileged EXEC** (`#`):

* **`show ip eigrp neighbors`**: Mostra i router vicini con cui stai scambiando informazioni.
* **`show ip route`**: Verifica che le reti remote appaiano precedute dalla lettera **D** (che indica EIGRP).
* **`show ip protocols`**: Per vedere i dettagli del protocollo, come i valori K e l'ID dell'AS.

---

### Un piccolo consiglio da "pro":
Se i router non comunicano, controlla prima il comando `show ip interface brief`. Se le interfacce sono "down", il protocollo di routing non potrà mai funzionare! Inoltre, assicurati che il numero del sistema autonomo (nell'esempio il `10`) sia identico ovunque.