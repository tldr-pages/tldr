# adig

> Wyświetla informacje otrzymane z serwerów DNS (Domain Name System).
> Więcej informacji: <https://manned.org/adig>.

- Wyświetl rekord A (domyślny) z DNS dla hosta(-ów):

`adig {{example.com}}`

- Wyświetl dodatkowe wyjście [d]ebugowania:

`adig -d {{example.com}}`

- Podłącz do określonego [s]erwera DNS:

`adig -s {{1.2.3.4}} {{example.com}}`

- Użyj określonego portu TCP łącząc się do serwera DNS:

`adig -T {{port}} {{example.com}}`

- Użyj określonego portu UDP łącząc się do serwera DNS:

`adig -U {{port}} {{example.com}}`
