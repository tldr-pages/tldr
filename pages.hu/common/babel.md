# babel

> Egy transzpiler, amely a JavaScript ES6/ES7 szintaxisból ES5 szintaxisba konvertálja a kódot. További információ: <https://babeljs.io/>.

- Egy megadott bemeneti fájl transzpilezése és kimenete a `stdout`:

`babel {{path/to/file}}`

- Egy megadott bemeneti fájl transzpilezése és kimenete egy adott fájlba:

`babel {{path/to/input_file}} --out-file {{path/to/output_file}}`

- A bemeneti fájl transzpilezése minden egyes módosításkor:

`babel {{path/to/input_file}} --watch`

- Egy egész könyvtárnyi fájl átfordítása:

`babel {{path/to/input_directory}}`

- Megadott, vesszővel elválasztott fájlok figyelmen kívül hagyása egy könyvtárban:

`babel {{path/to/input_directory}} --ignore {{ignored_files}}`

- Átfordítás és kimenet kicsinyített JavaScriptként:

`babel {{path/to/input_file}} --minified`

- Előbeállítások kiválasztása a kimeneti formázás számára:

`babel {{path/to/input_file}} --presets {{presets}}`

- Az összes rendelkezésre álló opció kiadása:

`babel --help`
