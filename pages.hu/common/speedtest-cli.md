# speedtest-cli

> Nem hivatalos parancssori interfész az internetes sávszélesség teszteléséhez a https://speedtest.net segítségével. A hivatalos CLI-t lásd még: `speedtest`. További információ: <https://github.com/sivel/speedtest-cli>.

- Futtasson sebességtesztet:

`speedtest-cli`

- Futtasson sebességtesztet, és bitek helyett bájtokban jelenítse meg az értékeket:

`speedtest-cli --bytes`

- Futtasson sebességtesztet a `HTTPS` használatával a `HTTP` helyett:

`speedtest-cli --secure`

- Sebességteszt futtatása letöltési tesztek elvégzése nélkül:

`speedtest-cli --no-download`

- Sebességteszt futtatása és az eredmények képének generálása:

`speedtest-cli --share`

- A `speedtest.net` összes szerverének listája, távolság szerint rendezve:

`speedtest-cli --list`

- Sebességteszt futtatása egy adott speedtest.net szerverre:

`speedtest-cli --server {{server_id}}`

- Sebességteszt futtatása és az eredmények JSON-ként történő megjelenítése (a haladási információk elnyomása):

`speedtest-cli --json`
