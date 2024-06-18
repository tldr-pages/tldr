# groupadd

> Voeg gebruikersgroepen toe aan het systeem.
> Bekijk ook: `groups`, `groupdel`, `groupmod`.
> Meer informatie: <https://manned.org/groupadd>.

- Maak een nieuwe groep aan:

`sudo groupadd {{groepsnaam}}`

- Maak een nieuwe systeemgroep aan:

`sudo groupadd --system {{groepsnaam}}`

- Maak een nieuwe groep aan met een specifieke groeps-ID:

`sudo groupadd --gid {{id}} {{groepsnaam}}`
