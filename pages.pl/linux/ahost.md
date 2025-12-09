# ahost

> Narzędzie zapytań DNS do wyświetlania rekordów A lub AAAA powiązanych z nazwą hosta lub adresem IP.
> Więcej informacji: <https://manned.org/ahost>.

- Wyświetl rekord `A` lub `AAAA` powiązany z nazwą hosta lub adresem IP::

`ahost {{example.com}}`

- Wyświetl dodatkowe wyjście debugowe:

`ahost -d {{example.com}}`

- Wyświetl rekord wskazanego typu:

`ahost -t {{a|aaaa|u}} {{example.com}}`
