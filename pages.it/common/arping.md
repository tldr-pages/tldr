# arping

> Scopri e interroga host in una rete utilizzando il protocollo ARP.
> Utile per scoprire indirizzi MAC.
> Maggiori informazioni: <https://github.com/ThomasHabets/arping>.

- Invia un ping ad un host inviando pacchetti ARP request:

`arping {{ip_host}}`

- Invia un pint ad un host su una specifica interfaccia:

`arping -I {{interfaccia}} {{ip_host}}`

- Invia un ping ad un host e termina all prima risposta:

`arping -f {{ip_host}}`

- Invia uno specifico numero di ping:

`arping -c {{count}} {{ip_host}}`

- Invia pacchetti ARP request in broadcast per aggiornare la cache ARP dei vicini:

`arping -U {{ip_da_inviare_in_broadcast}}`

- Rileva indirizzi IP duplicati nella rete inviando richieste ARP con un timeout di 3 secondi:

`arping -D -w {{3}} {{ip_da_controllare}}`
