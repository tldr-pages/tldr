# trust

> Eszköz a megbízhatósági szabályzat tárolójának működtetéséhez. További információ: <https://manned.org/trust>.

- A bizalmi házirend-tároló elemeinek listázása:

`trust list`

- A megbízhatósági házirend-tároló egyes elemeire vonatkozó információk listázása:

`trust list --filter={{blocklist|ca-anchors|certificates|trust-policy}}`

- Egy adott bizalmi horgony tárolása a bizalmi házirend-tárolóban:

`trust anchor {{path/to/certificate.crt}}`

- Egy adott horgony eltávolítása a megbízhatósági házirend tárolójából:

`trust anchor --remove {{path/to/certificate.crt}}`

- Bizalmi házirend kivonása a megosztott bizalmi házirend-tárolóból:

`trust extract --format=x509-directory --filter=ca-anchors {{path/to/directory}}`

- Súgó megjelenítése egy alparancshoz:

`trust {{subcommand}} --help`
