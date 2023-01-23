# carbon-now

> Készítsen gyönyörű képeket a kódról. További információ: <https://github.com/mixn/carbon-now-cli>.

- Kép létrehozása egy fájlból az alapértelmezett beállítások használatával:

`carbon-now {{path/to/file}}`

- Kép létrehozása a vágólapon lévő szövegből az alapértelmezett beállítások használatával:

`carbon-now --from-clipboard`

- Kép létrehozása standard bemenetről alapértelmezett beállításokkal:

`{{input}} | carbon-now`

- Képek létrehozása interaktívan egyéni beállításokkal, és opcionálisan menthet egy előre beállított képet:

`carbon-now -i {{path/to/file}}`

- Képek létrehozása korábban elmentett előbeállításból:

`carbon-now -p {{preset}} {{path/to/file}}`

- Megadott szövegsorral való kezdés:

`carbon-now -s {{line}} {{path/to/file}}`

- A szöveg egy adott soránál végződik:

`carbon-now -e {{line}} {{path/to/file}}`

- Kép megnyitása böngészőben mentés helyett:

`carbon-now --open {{path/to/file}}`
