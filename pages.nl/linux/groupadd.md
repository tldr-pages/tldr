# groupadd

> Voeg gebruikersgroepen toe aan het systeem.
> Zie ook: `groups`, `groupdel`, `groupmod`.
> Meer informatie: <https://manned.org/groupadd>.

- Maak een nieuwe groep aan:

`sudo groupadd {{groepsnaam}}`

- Maak een nieuwe systeemgroep aan:

`sudo groupadd {{[-r|--system]}} {{groepsnaam}}`

- Maak een nieuwe groep aan met een specifieke groeps-ID:

`sudo groupadd {{[-g|--gid]}} {{id}} {{groepsnaam}}`
