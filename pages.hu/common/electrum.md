# electrum

> Ergonomikus Bitcoin tárca és privát kulcsok kezelése. További információ: <https://electrum.org>.

- Új pénztárca létrehozása:

`electrum -w {{new_wallet.dat}} create`

- Meglévő pénztárca visszaállítása magról offline:

`electrum -w {{recovery_wallet.dat}} restore -o`

- Aláírt tranzakció létrehozása offline:

`electrum mktx {{recipient}} {{amount}} -f 0.0000001 -F {{from}} -o`

- Az összes tárca fogadó címének megjelenítése:

`electrum listaddresses -a`

- Üzenet aláírása:

`electrum signmessage {{address}} {{message}}`

- Üzenet hitelesítése:

`electrum verifymessage {{address}} {{signature}} {{message}}`

- Csatlakozás csak egy adott electrum-kiszolgáló példányhoz:

`electrum -p socks5:{{127.0.0.1}}:9050 -s {{56ckl5obj37gypcu.onion}}:50001:t -1`
