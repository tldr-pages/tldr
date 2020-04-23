# arp

> Pokaż i manipuluj pamięcią podręczną ARP systemu.

- Pokaż bieżącą tabelę arp:

`arp -a`

- Wyczyść całość cache:

`sudo arp -a -d`

- Usuń konkretny wpis:

`arp -d {{adres}}`

- Utwórz wpis:

`arp -s {{adres}} {{adres_mac}}`
