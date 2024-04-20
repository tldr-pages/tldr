# php

> Interfejs wiersza poleceń PHP.
> Więcej informacji: <https://php.net>.

- Parsuj i uruchom skrypt PHP:

`php {{plik}}`

- Sprawdź składnię skryptu PHP (np. lint):

`php -l {{plik}}`

- Uruchom PHP interaktywnie:

`php -a`

- Uruchom kod PHP (uwagi: nie używaj znaczników <? ?> ; unikaj podwójnych cudzysłowów z odwrotnym ukośnikiem):

`php -r "{{kod}}"`

- Uruchom wbudowany serwer PHP w bieżącym katalogu:

`php -S {{host:port}}`

- Uzyskaj listę zainstalowanych rozszerzeń PHP:

`php -m`

- Wyświetl informacje o bieżącej konfiguracji PHP:

`php -i`

- Wyświetl informacje o konkretnej funkcji:

`php --rf {{nazwa_funkcji}}`
