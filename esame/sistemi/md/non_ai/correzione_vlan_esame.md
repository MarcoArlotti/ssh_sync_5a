giornale locale = piccola azienda = poco budget
per separare il traffico si usa la vlan.

uso di portatili = DHCP + WLAN
banca dati protetta = DMZ
WEB server = passanole porte http 80 e https 443.

1. risale agli anni novanta, si rifa' come ci pare, partendo da 0.
2. la rete e' LAN + WLAN.
3. topologia stella estesa, scalabile aumentando la dimensione senza problemi.

## IL ROUTER
NAT dinamico (2 indirizzi pubblici) basta al posto che il PAT, il PAT e'molto costoso lato computazinale.

## FIREWALL
firewall extenal -> collegata la dmz
firewall internal

## DMZ
web server ->
dhcp server ->
db banca dati ->

## SWITCH / switch L3
Non colleghiamo ogniposto usando switch separati perche usiamo STP, massimo usiamo 43 porte, alcuni arrivano anche a 50.
Poi dividiamo in VALN

## CABLAGGIO
si prevede fibra ottica tra ISP e router, dentro alla rete al massimo usiamo i cavi cat buoni.

## WIRELESS
