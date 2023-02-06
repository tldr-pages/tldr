# lslocks

> A helyi rendszerzárak listázása. További információ: <https://manned.org/lslocks>.

- Az összes helyi rendszerzár listázása:

`lslocks`

- Zárak listázása meghatározott oszlopcímekkel:

`lslocks --output {{PID}},{{COMMAND}},{{PATH}}`

- Nyers kimenetet (oszlopok nélkül) produkáló zárak listázása oszlopfejlécek nélkül:

`lslocks --raw --noheadings`

- Zárolások listázása PID-bemenet szerint:

`lslocks --pid {{PID}}`

- JSON-kimenettel rendelkező zárak listázása a `stdout` címen:

`lslocks --json`
