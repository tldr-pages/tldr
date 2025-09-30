# arp

> Pokaż i manipuluj systemową pamięcią podręczną ARP.
> Więcej informacji: <https://manned.org/arp.8>.

- Pokaż bieżącą tabelę ARP:

`arp -a`

- Usuń konkretny wpis:

`arp -d {{adres}}`

- Utwórz nowy wpis w tabeli ARP:

`arp -s {{adres}} {{adres_mac}}`
