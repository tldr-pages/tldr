# bitcoin-cli

> Klient konsolowy do interakcji z demonem Bitcoina poprzez zapytania RPC.
> Używa konfiguracji zdefiniowanej w `bitcoin.conf`.
> Więcej informacji: <https://en.bitcoin.it/wiki/Running_Bitcoin#Command-line_arguments>.

- Wyślij transakcję na dany adres:

`bitcoin-cli sendtoaddress "{{adres}}" {{ilość}}`

- Wygeneruj jeden lub więcej bloków:

`bitcoin-cli generate {{ilość_bloków}}`

- Wyświetl informacje o portfelu:

`bitcoin-cli getwalletinfo`

- Wyświetl wszystkie poprzednie transakcje dostępne do opłacenia transakcji wychodzących:

`bitcoin-cli listunspent`

- Wyeksportuj dane portfela do pliku tekstowego:

`bitcoin-cli dumpwallet "{{ścieżka/do/pliku}}"`
