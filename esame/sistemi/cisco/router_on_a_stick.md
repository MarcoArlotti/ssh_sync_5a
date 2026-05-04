 Es_3 
 Crea una rete così composta usando solo i comandi da  CLI:  
 2 
  hosts+ 1 switch rete Vlan 10 +2 hosts+ 1 switch rete Vlan 20,collegati  
 ad un unico switch e configurali secondo la modalità corretta . 
 Esegui la diagnostica 


 devo creare questa rete su cisco packet ndo solo la cli, fammi tutto passo per passo 

 descrivendo ogni passaggio attentamente senza saltare niente



Certamente. Creare una rete VLAN basata su CLI in Cisco Packet Tracer è un ottimo esercizio per comprendere la segmentazione di rete.

### Topologia di Rete
Per questo esercizio, immagina questa disposizione su Packet Tracer:
* **Switch 1 (Accesso VLAN 10)**: Collegato a 2 PC.
* **Switch 2 (Accesso VLAN 20)**: Collegato a 2 PC.
* **Switch Centrale (Core)**: Collega Switch 1 e Switch 2 tra loro.

[Immagine di una topologia di rete stella con switch centrale]

---

### Preparazione Fisica
Prima di iniziare con la CLI, trascina nell'area di lavoro:
1.  **3 Switch** (es. modello 2960).
2.  **4 PC**.
3.  **Cavi**: Usa il cavo "Copper Straight-Through" per collegare i PC agli switch e gli switch tra loro (Packet Tracer gestisce l'auto-MDIX, quindi non preoccuparti se usi cavi diretti anche tra switch).

---

### Configurazione Switch 1 (VLAN 10)
Questo switch gestirà solo la VLAN 10.
*Apri lo Switch 1 > tab CLI > premi Invio.*

```text
enable
configure terminal
hostname SW-VLAN10

! Creazione della VLAN
vlan 10
name UFFICIO
exit

! Configurazione porte verso i PC (es. FastEthernet 0/1 e 0/2)
interface range fa0/1 - 2
switchport mode access
switchport access vlan 10
exit

! Configurazione porta uplink verso lo Switch Centrale (es. FastEthernet 0/24)
interface fa0/24
switchport mode trunk
exit
```

---

### Configurazione Switch 2 (VLAN 20)
Questo switch gestirà solo la VLAN 20.
*Apri lo Switch 2 > tab CLI.*

```text
enable
configure terminal
hostname SW-VLAN20

! Creazione della VLAN
vlan 20
name OSPITI
exit

! Configurazione porte verso i PC (es. FastEthernet 0/1 e 0/2)
interface range fa0/1 - 2
switchport mode access
switchport access vlan 20
exit

! Configurazione porta uplink verso lo Switch Centrale (es. FastEthernet 0/24)
interface fa0/24
switchport mode trunk
exit
```

---

### Configurazione Switch Centrale (Core)
Questo switch deve conoscere entrambe le VLAN e gestire i trunk.
*Apri lo Switch Centrale > tab CLI.*

```text
enable
configure terminal
hostname SW-CORE

! Creazione di entrambe le VLAN
vlan 10
name UFFICIO
exit
vlan 20
name OSPITI
exit

! Configurazione porte verso i due switch di accesso (es. fa0/1 e fa0/2)
interface range fa0/1 - 2
switchport mode trunk
exit
```

---

### Configurazione Indirizzi IP (PC)
Poiché nei PC di Packet Tracer non si configura l'IP tramite CLI, dovrai andare su ogni PC:
1.  Clicca sul PC > Tab **Desktop** > **IP Configuration**.
2.  Assegna gli IP manualmente (esempio):

| Dispositivo | Indirizzo IP | Subnet Mask |
| :--- | :--- | :--- |
| PC1 (VLAN 10) | 192.168.10.2 | 255.255.255.0 |
| PC2 (VLAN 10) | 192.168.10.3 | 255.255.255.0 |
| PC3 (VLAN 20) | 192.168.20.2 | 255.255.255.0 |
| PC4 (VLAN 20) | 192.168.20.3 | 255.255.255.0 |

*Nota: Non abbiamo inserito un Gateway perché, senza un router, la comunicazione è limitata all'interno della stessa VLAN.*

---

### Diagnostica
Ora verifichiamo che la configurazione sia corretta usando i comandi di verifica.

#### 1. Verifica VLAN e Porte sugli Switch
Sullo `SW-VLAN10` e `SW-VLAN20`, digita:
`show vlan brief`
*Dovresti vedere la VLAN 10 (o 20) associata alle interfacce corrette.*

#### 2. Verifica Trunk sullo Switch Centrale
Sullo `SW-CORE`, digita:
`show interfaces trunk`
*Dovresti vedere le porte fa0/1 e fa0/2 con stato "trunking" e le VLAN 10 e 20 elencate come consentite.*

#### 3. Test di Connettività (Ping)
Vai su **PC1** (192.168.10.2) > **Desktop** > **Command Prompt**:

* **Test interno VLAN 10**:
    `ping 192.168.10.3`
    *Dovrebbe avere successo (Reply).*

* **Test tra VLAN 10 e 20**:
    `ping 192.168.20.2`
    *Dovrebbe fallire ("Request timed out").*

Questo comportamento è corretto: le VLAN sono segmentate. Per farle comunicare tra loro avresti bisogno di un router (o uno switch Layer 3) configurato per l'Inter-VLAN routing.

Hai bisogno di aiuto per configurare il routing tra queste due VLAN?

---


Per far comunicare le VLAN che abbiamo appena creato, il metodo più comune e scalabile in Cisco Packet Tracer è il cosiddetto **Router-on-a-Stick**.

In questa configurazione, usiamo un unico cavo fisico tra lo Switch Centrale e il Router, ma lo dividiamo logicamente in più **sotto-interfacce** (sub-interfaces), una per ogni VLAN.

---

### 1. Collegamento Fisico
1.  Trascina un **Router 2911** (o un 4331) nell'area di lavoro.
2.  Collega la porta **GigabitEthernet 0/0** del Router a una porta libera dello **Switch Centrale** (es. GigabitEthernet 0/1).

---

### 2. Configurazione dello Switch Centrale (Trunk verso il Router)
Dobbiamo dire allo switch che la porta collegata al router deve lasciar passare tutto il traffico delle VLAN.

```text
enable
configure terminal
interface gi0/1
 switchport mode trunk
 exit
```

---

### 3. Configurazione del Router (CLI)
Qui avviene la "magia". Non diamo un IP all'interfaccia fisica, ma creiamo delle interfacce virtuali.
*Apri il Router > tab CLI.*



```text
enable
configure terminal
hostname R1

! Attiviamo l'interfaccia fisica (senza assegnare IP)
interface gigabitEthernet 0/0
 no shutdown
 exit

! --- Sotto-interfaccia per VLAN 10 ---
interface gigabitEthernet 0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
 exit

! --- Sotto-interfaccia per VLAN 20 ---
interface gigabitEthernet 0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
 exit
```

#### Spiegazione dei comandi:
* **`interface g0/0.10`**: Crea un'interfaccia virtuale per la VLAN 10.
* **`encapsulation dot1Q 10`**: Dice al router di usare il protocollo 802.1Q per leggere i "tag" della VLAN 10.
* **`ip address`**: Questo diventerà il **Default Gateway** per i PC della rispettiva VLAN.

---

### 4. Configurazione dei PC (Passaggio Fondamentale)
Affinché i PC sappiano come inviare pacchetti fuori dalla propria rete, devi impostare il **Default Gateway** nelle impostazioni IP di ogni PC (Tab Desktop > IP Configuration):

| Dispositivo | Indirizzo IP | Default Gateway |
| :--- | :--- | :--- |
| **PC1 (VLAN 10)** | 192.168.10.2 | **192.168.10.1** |
| **PC2 (VLAN 10)** | 192.168.10.3 | **192.168.10.1** |
| **PC3 (VLAN 20)** | 192.168.20.2 | **192.168.20.1** |
| **PC4 (VLAN 20)** | 192.168.20.3 | **192.168.20.1** |

---

### 5. Diagnostica Finale
Ora che il router è attivo, i due mondi possono comunicare.

1.  **Test Inter-VLAN**:
    Apri il Command Prompt di **PC1** (VLAN 10) e prova a pingare **PC3** (VLAN 20):
    `ping 192.168.20.2`
    *Nota: Il primo o secondo pacchetto potrebbero fallire per via della risoluzione ARP, ma i successivi devono dare "Reply".*

2.  **Verifica Tabella di Routing**:
    Sul Router, digita:
    `show ip route`
    *Dovresti vedere le reti 192.168.10.0 e 192.168.20.0 come "Directly Connected" tramite le sotto-interfacce.*

3.  **Tracciamento del percorso**:
    Sempre dal PC1, digita:
    `tracert 192.168.20.2`
    *Vedrai che il pacchetto passa prima per il gateway (192.168.10.1) e poi arriva a destinazione.*

Vuoi approfondire come limitare il traffico tra queste VLAN usando le ACL (Access Control Lists) o preferisci vedere come si configura uno Switch Layer 3 per fare la stessa cosa senza router?