# ncat

> Használja a normál `cat` funkciót a hálózatokon keresztül. További információ: <https://manned.org/ncat>.

- Figyel a megadott porton történő bemenetre, és írja azt a megadott fájlba:

`ncat -l {{port}} > {{path/to/file}}`

- Több kapcsolat fogadása és az ncat nyitva tartása azok lezárása után:

`ncat -lk {{port}}`

- A megadott fájl kimeneteinek írása a megadott porton a megadott állomáson:

`ncat {{address}} {{port}} < {{path/to/file}}`
