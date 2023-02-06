# bitcoin-cli

> Parancssori ügyfél a Bitcoin-démonnal való interakcióhoz RPC-hívásokon keresztül. A `bitcoin.conf` oldalon meghatározott konfigurációt használja. További információ: <https://en.bitcoin.it/wiki/Running_Bitcoin#Command-line_arguments>.

- Tranzakció küldése egy adott címre:

`bitcoin-cli sendtoaddress "{{address}}" {{amount}}`

- Egy vagy több blokk generálása:

`bitcoin-cli generate {{num_blocks}}`

- Magas szintű információk nyomtatása a tárcáról:

`bitcoin-cli getwalletinfo`

- A korábbi tranzakciók összes kimenő tranzakciójának listája, amely a kimenő tranzakciók finanszírozásához rendelkezésre áll:

`bitcoin-cli listunspent`

- A pénztárca információinak exportálása szöveges fájlba:

`bitcoin-cli dumpwallet "{{path/to/file}}"`
