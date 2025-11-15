# adig

> Wyświetl informacje otrzymane z serwerów DNS (Domain Name System).
> Więcej informacji: <https://manned.org/adig>.

- Wyświetl rekord A (domyślny) z DNS dla hosta(-ów):

`adig {{example.com}}`

- Wyświetl dodatkowe wyjście [d]ebugowania:

`adig -d {{example.com}}`

- Połącz z określonym [s]erwerem DNS:

`adig -s {{1.2.3.4}} {{example.com}}`

- Użyj określonego portu TCP łącząc się z serwerem DNS:

`adig -T {{port}} {{example.com}}`

- Użyj określonego portu UDP łącząc się z serwerem DNS:

`adig -U {{port}} {{example.com}}`
