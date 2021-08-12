# arping

> Descoperiţi şi sondează gazdele într-o reţea utilizând protocolul ARP.
> Util pentru descoperirea adresei MAC.
> Mai multe informaţii: <https://github.com/ThomasHabets/arping>

- Ping o gazdă de pachete de cerere ARP:

`arping {{host_ip}}`

- Ping o gazdă pe o anumită interfață:

`arping -I {{interface}} {{host_ip}}`

- Ping o gazdă și opri la primul răspuns:

`arping -f {{host_ip}}`

- Ping o gazdă de un anumit număr de ori:

`arping -c {{count}} {{host_ip}}`

- Broadcast ARP cerere pachete pentru a actualiza cache-urile ARP ale vecinilor:

`arping -U {{ip_to_broadcast}}`

- Detectați adresele IP duplicate în rețea prin trimiterea de cereri ARP cu un timeout de 3 secunde:

`arping -D -w {{3}} {{ip_to_check}}`
