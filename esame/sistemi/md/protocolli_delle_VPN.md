# protocolli delle VPN
Ecco una panoramica tecnica dei protocolli VPN e delle strategie di implementazione per un contesto aziendale.

---

# Protocolli VPN e Implementazione Aziendale

La scelta del protocollo VPN determina l'equilibrio tra **sicurezza**, **velocità** e **compatibilità**. In un'infrastruttura aziendale, questa scelta deve riflettere le necessità di accesso remoto dei dipendenti e l'interconnessione tra sedi diverse.

## 1. Analisi dei Protocolli VPN

### **OpenVPN**
È lo standard de facto del settore per la sua flessibilità. È un protocollo open-source che utilizza la libreria OpenSSL per la crittografia.
* **Vantaggi:** Estremamente sicuro, può operare su qualsiasi porta (bypassando i firewall tramite la porta 443/HTTPS).
* **Svantaggi:** Richiede software client di terze parti; può risultare più lento a causa dell'elevato overhead computazionale.

### **IPsec (Internet Protocol Security)**
Spesso utilizzato in combinazione con IKEv2 (Internet Key Exchange version 2). È la scelta primaria per le connessioni **Site-to-Site**.
* **Vantaggi:** Molto veloce e stabile (gestisce bene i cambi di rete, come il passaggio da Wi-Fi a 4G). Supportato nativamente da quasi tutti i sistemi operativi moderni.
* **Svantaggi:** Più facile da bloccare da parte dei firewall rispetto a OpenVPN.



### **WireGuard**
Il protocollo di nuova generazione che sta rivoluzionando il settore.
* **Vantaggi:** Codice estremamente snello (circa 4.000 righe contro le 600.000 di OpenVPN), velocità superiori e latenza minima.
* **Svantaggi:** Più recente, richiede configurazioni specifiche per la gestione dinamica degli IP in ambito aziendale (Privacy/Logging).

### **SSTP (Secure Socket Tunneling Protocol)**
Protocollo proprietario di Microsoft.
* **Vantaggi:** Integrazione perfetta con l'ecosistema Windows; utilizza la porta 443, rendendolo quasi impossibile da bloccare.
* **Svantaggi:** Scarsa compatibilità con dispositivi non-Windows.

---

## 2. Strategie di Implementazione in Rete Aziendale

L'implementazione deve seguire una gerarchia di sicurezza rigorosa per proteggere le risorse interne.

### **A. Architettura Remote Access (Client-to-Site)**
Utilizzata per permettere ai lavoratori in smart working di accedere alla LAN aziendale.
1.  **Terminazione della VPN:** La VPN non deve terminare direttamente sul Domain Controller, ma su un **Firewall Next-Gen (NGFW)** o un concentratore VPN dedicato in una **DMZ**.
2.  **Autenticazione Multi-Fattore (MFA):** Obbligatoria. L'accesso deve richiedere una credenziale (LDAP/Active Directory) più un token temporaneo (TOTP).
3.  **Split Tunneling vs Full Tunneling:** * *Full Tunneling:* Tutto il traffico passa per l'azienda (massima sicurezza, alto consumo di banda).
    * *Split Tunneling:* Solo il traffico destinato ai server aziendali passa per la VPN (migliori performance).

### **B. Architettura Site-to-Site**
Utilizzata per collegare due sedi fisiche (es. Sede Centrale e Filiale).
* Si implementano **Tunnel IPsec permanenti** tra i router/firewall di confine.
* La crittografia raccomandata è **AES-256** con algoritmi di hashing **SHA-256** o superiori.



---

## 3. Best Practices per la Sicurezza

* **Principio del Minimo Privilegio:** Una volta connesso, l'utente non deve vedere tutta la rete, ma solo le risorse necessarie (utilizzando VLAN e ACL).
* **Logging e Monitoring:** Tracciare ogni sessione VPN, monitorando orari di accesso e volumi di traffico per identificare anomalie.
* **Aggiornamenti:** Mantenere il firmware dei gateway VPN sempre aggiornato per prevenire vulnerabilità note (es. CVE su SSL-VPN).

---

### Prossimi passi consigliati
Ti serve aiuto per configurare una specifica regola di firewalling per un tunnel IPsec o preferisci approfondire come integrare l'autenticazione RADIUS con la tua VPN?