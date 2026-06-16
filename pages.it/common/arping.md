# arping

> Scopri e interroga host in una rete utilizzando il protocollo ARP.
> Utile per scoprire indirizzi MAC.
> Maggiori informazioni: <https://manned.org/arping>.

- Invia un ping ad un host inviando pacchetti ARP request:

`sudo arping {{ip_host}}`

- Invia un pint ad un host su una specifica interfaccia:

`sudo arping -I {{interfaccia}} {{ip_host}}`

- Invia un ping ad un host e termina all prima risposta:

`sudo arping -f {{ip_host}}`

- Invia uno specifico numero di ping:

`sudo arping -c {{count}} {{ip_host}}`

- Invia pacchetti ARP request in broadcast per aggiornare la cache ARP dei vicini:

`sudo arping -U {{ip_da_inviare_in_broadcast}}`

- Rileva indirizzi IP duplicati nella rete inviando richieste ARP con un timeout di 3 secondi:

`sudo arping -D -w {{3}} {{ip_da_controllare}}`
