# speedtest

> Hivatalos parancssori felület az internetes sávszélesség teszteléséhez a <https://speedtest.net> segítségével.
> Megjegyzés: egyes platformok a `speedtest` és a `speedtest-cli` közötti linket tartalmazzák.
> Ha az oldalon található példák közül néhány nem működik, lásd a `speedtest-cli`.
> További információ: <https://www.speedtest.net/apps/cli>.

- Futtasson sebességtesztet:

`speedtest`

- Futtasson sebességtesztet, és adja meg a kimenet egységét:

`speedtest --unit={{auto-decimal-bits|auto-decimal-bytes|auto-binary-bits|auto-binary-bytes}}`

- Futtasson sebességtesztet, és adja meg a kimenet formátumát:

`speedtest --format={{human-readable|csv|tsv|json|jsonl|json-pretty}}`

- Futtasson sebességtesztet, és adja meg a tizedesjegyek számát (0-tól 8-ig, alapértelmezett érték 2):

`speedtest --precision={{precision}}`

- Sebességteszt futtatása és annak előrehaladásának kinyomtatása (csak a `human-readable` és a `json` kimeneti formátum esetén érhető el):

`speedtest --progress={{yes|no}}`

- Az összes `speedtest.net` kiszolgáló listája, távolság szerint rendezve:

`speedtest --servers`

- Sebességteszt futtatása egy adott `speedtest.net` szerverhez:

`speedtest --server-id={{server_id}}`
