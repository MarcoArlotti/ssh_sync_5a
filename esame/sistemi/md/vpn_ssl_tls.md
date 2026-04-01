# SSL/TLS VPN
Esistono in alternativa di IPsec,
Viene usato nello strato SESSION, non supporta UDP.
Nasce da Netscape.
Usa il record protocol e l'hanshacke protocol.

# L'hanshake
Solo il server si deve autenticare invece il client non e' obbligato.
Sfrutta una certification authorities
che nel processo dell'invio e' detto invio della
PRE MASTER KEY, Le public key le mettiamo nelle certification authorities,
per verificare che la chiave pubblica inviata non puo' essere falsificata facendo da MAN IN THE MIDDLE.

Quindi risolve il problema di IPsec, nel dover autenticare sia client che server.