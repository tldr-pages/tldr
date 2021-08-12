# bitcoin-cli

> Client de linie de comandă pentru a interacționa cu daemonul Bitcoin prin apeluri RPC.
> Utilizează configurația definită în `bitcoin.conf`.
> Mai multe informaţii: <https://en.bitcoin.it/wiki/Running_Bitcoin#Command-line_arguments>

- Trimiteți o tranzacție la o anumită adresă:

`bitcoin-cli sendtoaddress "{{address}}" {{amount}}`

- Generează unul sau mai multe blocuri:

`bitcoin-cli generate {{num_blocks}}`

- Imprimați informații de nivel înalt despre portofel:

`bitcoin-cli getwalletinfo`

- Lista tuturor ieșirilor din tranzacțiile anterioare disponibile pentru finanțarea tranzacțiilor efectuate:

`bitcoin-cli listunspent`

- Exportați informațiile portofel într-un fișier text:

`bitcoin-cli dumpwallet "{{path/to/file}}"`
