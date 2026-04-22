# LE VPN
Le VPN nascono per collegare piu' aziende o singoli dipendenti alla rete privata di una sede principale di una azienda proprio come se fossero collegati fisicamente alla rete.

>aprendo le porte allo SMART WORKING, cioe' un dipendente che lavore da remoto.

La parte piu' importante di una VPN e' la sicurezza,
per collegare insieme le sedi al posto che piazzare un cavo fisico, molto costoso e che rischia danneggiamenti, si crea un collegamento logico tramite la rete pubblica come mezzo, ma introducono problemi come la ridotta lentezza e costi della banda usata.

Nel fare passare i pacchetti nella rete pubblica, e' fondamentale:
- applicare una cifratura,
- controllo degli accessi (autenticazione),
- tunneling dei pacchetti.

---

## Le varie classificazioni
Esistono 2 tipi principali di VPN:

## 1. REMOTE-ACCESS VPN
>Ha la funzione principale di desktop remoto per collegarsi alla LAN della sede principale,
>E' soprattutto usata per collegare piccole sedi o pochi dipendenti alla LAN principale.

I singoli utenti si collegano ad un server di accesso detto NAS
> NAS (NETWORK ACCESS SERVER)  che puo' essere dell'HARWARE dedicato o una semplice applicazione eseguita in un server condiviso.
>
>Il NAS chiede le credenziali all'utente, che se valide, gli permettera' di usare la VPN.

Il *NAS* per verificare la autenticazione puo' appoggiarsi ad un `RADIUS AAA SERVER` che lo fa al posto suo.
***AAA*** sta per:
- `Authentication` (verifica gli accessi),
- `Authorization` (verifica cio' che e' permesso),
- `Accounting` (tiene tracci adi chi fa che cosa {non ripiudabilita'}).

In piu' per funzionare, il client dovra' munirsi di un software VPN client.

>l'affitto di un NAS e' detto ESP,
>L'ESP configura il NAS e lo mantiene funzionante a chi lo affittera'.

## 2. SITE-TO-SITE VPN
>Si usa principalmente per collegare 2 sedi grosse insieme permettendogli di condividere le risorse (stampanti, pc, archivio).

Le VPN site to site eliminano la necessita' di avere una applicazione client VPN per ogni CLIENT.

La SITE-TO-SITE VPN si divide principalmente in:
- INTRANET BASED:
    >Una rete intranet collega 2 sedi in una unica.
- EXTRANET BASED:
    >Se l'azienda ha un rapporto stretto con un altra azienda esterna, EXTRANET permette di lavorare insieme in modo sicuro condividendo le risorse, senza dando l'accesso completo a tutto.
