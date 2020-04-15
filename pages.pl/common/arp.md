# arp

> Pokaż i manipuluj pamięcią podręczną ARP systemu.

- Pokaż bieżącą tabelę arp:

`arp -a`

- Wyczyść całość cache:

`sudo arp -a -d`

- Usuń konkretny wpis:

`arp -d {{address}}`

- Utwórz wpis:

`arp -s {{address}} {{mac_address}}`
