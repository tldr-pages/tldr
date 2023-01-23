# atoum

> Egy egyszerű, modern és intuitív egységtesztelő keretrendszer PHP-hez. További információ [: http://atoum.org](http://atoum.org).

- Konfigurációs fájl inicializálása:

`atoum --init`

- Az összes teszt futtatása:

`atoum`

- A tesztek futtatása a megadott konfigurációs fájl használatával:

`atoum -c {{path/to/file}}`

- Egy adott tesztfájl futtatása:

`atoum -f {{path/to/file}}`

- Egy adott tesztkönyvtár futtatása:

`atoum -d {{path/to/directory}}`

- Az összes teszt futtatása egy adott névtér alatt:

`atoum -ns {{namespace}}`

- Az összes teszt futtatása egy adott címkével:

`atoum -t {{tag}}`

- Egyéni bootstrap fájl betöltése a tesztek futtatása előtt:

`atoum --bootstrap-file {{path/to/file}}`
