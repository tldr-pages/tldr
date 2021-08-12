# ipfs

> Sistem de fișiere interplanetare.
> Un protocol de hipermedia peer-to-peer. Scopul este de a face web-ul mai deschis.
> Mai multe informaţii: <https://ipfs.io>

- Adăugați un fișier de la local la sistemul de fișiere, fixați-l și imprimați hash-ul relativ:

`ipfs add {{filename}}`

- Adăugați un director și fișierele sale recursiv de la local la sistemul de fișiere și imprimați hash-ul relativ:

`ipfs add -r {{directory}}`

- Salvați un fișier la distanță și dați-i un nume, dar nu-l fixați:

`ipfs get {{hash}} -o {{filename}}`

- Fixați un fișier la distanță local:

`ipfs pin add {{hash}}`

- Afișează fișierele fixate:

`ipfs pin ls`

- Anularea fixării unui fișier din spațiul de stocare local:

`ipfs pin rm {{hash}}`

- Eliminați fișierele nefixate din spațiul de stocare local:

`ipfs repo gc`
