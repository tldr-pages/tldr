# netselect

> Test de viteză pentru alegerea unui server de rețea rapid.
> Mai multe informaţii: <https://github.com/apenwarr/netselect>

- Alegeți serverul cu cea mai mică latență:

`sudo netselect {{host_1}} {{host_2}}`

- Display server de nume rezoluție și statistici:

`sudo netselect -vv {{host_1}} {{host_2}}`

- Definiți TTL maxim (timp de trăit):

`sudo netselect -m {{10}} {{host_1}} {{host_2}}`

- Imprimați cele mai rapide servere N printre gazde:

`sudo netselect -s {{N}} {{host_1}} {{host_2}} {{host_3}}`

- Lista opțiunilor disponibile:

`netselect`
