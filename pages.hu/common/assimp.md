# assimp

> Az Open Asset Import Library parancssori kliense. 40+ 3D fájlformátum betöltését és számos népszerű 3D formátumba történő exportálását támogatja. További információ: <http://www.assimp.org/>.

- Az összes támogatott import formátum listája:

`assimp listext`

- Az összes támogatott export formátum felsorolása:

`assimp listexport`

- Egy fájl átalakítása a támogatott kimeneti formátumok egyikébe, az alapértelmezett paraméterek használatával:

`assimp export {{input_file.stl}} {{output_file.obj}}`

- Egy fájl átalakítása egyéni paraméterek használatával (az assimp forráskódjában található dox_cmd.h fájl felsorolja a rendelkezésre álló paramétereket):

`assimp export {{input_file.stl}} {{output_file.obj}} {{parameters}}`

- A 3D fájl tartalmának összefoglalójának megjelenítése:

`assimp info {{path/to/file}}`

- Az összes támogatott alparancs ("verbs") felsorolása:

`assimp help`

- Segítség kérése egy adott alparanccsal kapcsolatban (pl. a rá jellemző paraméterek):

`assimp {{subcommand}} --help`
