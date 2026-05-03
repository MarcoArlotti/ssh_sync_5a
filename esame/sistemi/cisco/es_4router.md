Ecco una guida completa e strutturata che raccoglie tutti i passaggi, i calcoli e i comandi necessari per realizzare da zero la rete richiesta su Cisco Packet Tracer.

---

# Relazione Tecnica: Implementazione Rete Multi-Router con VLSM

## 1. Analisi del Progetto e Subnetting (VLSM)
L'obiettivo è suddividere la rete di Classe C **192.168.4.0** per ospitare 4 LAN di dimensioni differenti (120, 60, 30, 10 host) e i collegamenti seriali tra i router. Per ottimizzare lo spazio si utilizza il **VLSM (Variable Length Subnet Mask)**, partendo dalla sottorete più grande.

### Tabella di Indirizzamento LAN
| LAN | Host Richiesti | Host Assegnati | CIDR | Subnet Mask | Indirizzo di Rete | Gateway (Router) | Range IP Utili (per PC) | Broadcast |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **LAN 1** | 120 | 128 | /25 | 255.255.255.128 | 192.168.4.0 | 192.168.4.1 | .2 - .126 | 192.168.4.127 |
| **LAN 2** | 60 | 64 | /26 | 255.255.255.192 | 192.168.4.128 | 192.168.4.129 | .130 - .190 | 192.168.4.191 |
| **LAN 3** | 30 | 32 | /27 | 255.255.255.224 | 192.168.4.192 | 192.168.4.193 | .194 - .222 | 192.168.4.223 |
| **LAN 4** | 10 | 16 | /28 | 255.255.255.240 | 192.168.4.224 | 192.168.4.225 | .226 - .238 | 192.168.4.239 |

### Tabella Collegamenti WAN (Router-Router)
Si utilizzano maschere **/30** (solo 2 IP utilizzabili) per i collegamenti punto-punto.
* **R1-R2:** 192.168.4.240/30 (IP: .241 e .242)
* **R2-R3:** 192.168.4.244/30 (IP: .245 e .246)
* **R3-R4:** 192.168.4.248/30 (IP: .249 e .250)

---

## 2. Allestimento su Packet Tracer
1.  **Dispositivi:** Trascina 4 Router (es. modello **2911**) e 4 Switch.
2.  **Moduli Seriali:**
    * Spegni ogni router (tasto fisico).
    * Trascina il modulo **HWIC-2T** nello slot vuoto.
    * Riaccendi il router.
3.  **Connessioni:**
    * Usa il cavo **Copper Straight-Through** per collegare la porta `GigabitEthernet 0/0` di ogni router al rispettivo switch.
    * Usa il cavo **Serial DCE** (rosso a zigzag) per collegare i router tra loro:
        * R1 (S0/3/0) <---> R2 (S0/3/0)
        * R2 (S0/3/1) <---> R3 (S0/3/0)
        * R3 (S0/3/1) <---> R4 (S0/3/0)

---

## 3. Configurazione CLI dei Router
Copia e incolla questi comandi nella scheda **CLI** di ogni router per impostare IP e Rotte Statiche.

### **Router 1 (LAN 120 host)**
```bash
Router> enable
Router# configure terminal
interface g0/0
 ip address 192.168.4.1 255.255.255.128
 no shutdown
exit
interface s0/3/0
 ip address 192.168.4.241 255.255.255.252
 no shutdown
exit
# Rotte verso le LAN 2, 3 e 4 via R2
ip route 192.168.4.128 255.255.255.192 192.168.4.242
ip route 192.168.4.192 255.255.255.224 192.168.4.242
ip route 192.168.4.224 255.255.255.240 192.168.4.242
do write
```

### **Router 2 (LAN 60 host)**
```bash
Router> enable
Router# configure terminal
interface g0/0
 ip address 192.168.4.129 255.255.255.192
 no shutdown
exit
interface s0/3/0
 ip address 192.168.4.242 255.255.255.252
 no shutdown
exit
interface s0/3/1
 ip address 192.168.4.245 255.255.255.252
 no shutdown
exit
# Rotta a sinistra (LAN 1) e a destra (LAN 3, 4)
ip route 192.168.4.0 255.255.255.128 192.168.4.241
ip route 192.168.4.192 255.255.255.224 192.168.4.246
ip route 192.168.4.224 255.255.255.240 192.168.4.246
do write
```

### **Router 3 (LAN 30 host)**
```bash
Router> enable
Router# configure terminal
interface g0/0
 ip address 192.168.4.193 255.255.255.224
 no shutdown
exit
interface s0/3/0
 ip address 192.168.4.246 255.255.255.252
 no shutdown
exit
interface s0/3/1
 ip address 192.168.4.249 255.255.255.252
 no shutdown
exit
# Rotte a sinistra (LAN 1, 2) e a destra (LAN 4)
ip route 192.168.4.0 255.255.255.128 192.168.4.245
ip route 192.168.4.128 255.255.255.192 192.168.4.245
ip route 192.168.4.224 255.255.255.240 192.168.4.250
do write
```

### **Router 4 (LAN 10 host)**
```bash
Router> enable
Router# configure terminal
interface g0/0
 ip address 192.168.4.225 255.255.255.240
 no shutdown
exit
interface s0/3/0
 ip address 192.168.4.250 255.255.255.252
 no shutdown
exit
# Rotte verso tutto ciò che sta a sinistra via R3
ip route 192.168.4.0 255.255.255.128 192.168.4.249
ip route 192.168.4.128 255.255.255.192 192.168.4.249
ip route 192.168.4.192 255.255.255.224 192.168.4.249
do write
```

---

## 4. Configurazione dei PC Finali
Per ogni PC aggiunto alla rete, vai su **Desktop > IP Configuration**:

* **PC in LAN 1:** IP `192.168.4.2`, Subnet `255.255.255.128`, Gateway `192.168.4.1`
* **PC in LAN 2:** IP `192.168.4.130`, Subnet `255.255.255.192`, Gateway `192.168.4.129`
* **PC in LAN 3:** IP `192.168.4.194`, Subnet `255.255.255.224`, Gateway `192.168.4.193`
* **PC in LAN 4:** IP `192.168.4.226`, Subnet `255.255.255.240`, Gateway `192.168.4.225`

---

## 5. Verifica e Troubleshooting
1.  **Il primo pacchetto fallisce:** È normale (protocollo ARP). Prova il ping una seconda volta.
2.  **Request Time Out:** * Verifica di aver scritto il **Default Gateway** corretto sui PC.
    * Usa il comando `show ip route` sui router per vedere se le rotte con la lettera **S** sono presenti.
    * Controlla che i cavi seriali siano "Up" (verdi). Se sono rossi, controlla il comando `no shutdown` sulle porte seriali.
3.  **Salvataggio:** Ricorda di usare il comando `write` o `copy run start` su ogni router per non perdere i dati al riavvio.