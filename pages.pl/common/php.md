# php

> Interfejs wiersza poleceń PHP.
> Więcej informacji: <https://www.php.net/manual/en/features.commandline.options.php>.

- Parsuj i uruchom skrypt PHP:

`php {{plik}}`

- Sprawdź składnię skryptu PHP (np. lint):

`php {{[-l|--syntax-check]}} {{plik}}`

- Uruchom PHP interaktywnie:

`php {{[-a|--interactive]}}`

- Uruchom kod PHP (uwagi: nie używaj znaczników <? ?> ; unikaj podwójnych cudzysłowów z odwrotnym ukośnikiem):

`php {{[-r|--run]}} "{{kod}}"`

- Uruchom wbudowany serwer PHP w bieżącym katalogu:

`php {{[-S|--server]}} {{host:port}}`

- Uzyskaj listę zainstalowanych rozszerzeń PHP:

`php {{[-m|--modules]}}`

- Wyświetl informacje o bieżącej konfiguracji PHP:

`php {{[-i|--info]}}`

- Wyświetl informacje o konkretnej funkcji:

`php {{[--rf|--rfunction]}} {{nazwa_funkcji}}`
