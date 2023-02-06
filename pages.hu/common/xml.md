# xml

> XMLStarlet eszközkészlet: Ez a parancs is rendelkezik dokumentációval az alparancsairól, pl. `xml validate`. További információ: <http://xmlstar.sourceforge.net/docs.php>.

- Általános súgó megjelenítése, beleértve az alparancsok listáját:

`xml --help`

- Egy alparancs végrehajtása egy fájlból vagy URI-ból származó bemenettel, nyomtatás a `stdout` címre:

`xml {{subcommand}} {{options}} {{path/to/input.xml|URI}}`

- Alparancs végrehajtása a `stdin` és a `stdout` használatával:

`xml {{subcommand}} {{options}}`

- Alparancs végrehajtása fájlból vagy URI-ból származó bemenettel és fájlba történő kimenettel:

`xml {{subcommand}} {{options}} {{path/to/input.xml|URI}} > {{path/to/output}}`

- Egy alparancs súgójának megjelenítése:

`xml {{subcommand}} --help`

- Az XMLStarlet Toolkit verziójának megjelenítése:

`xml --version`
