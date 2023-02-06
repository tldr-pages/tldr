# lebab

> JavaScript modernizáló a kód ES6/ES7-re történő átfordításához. A transzformációkat minden példához meg kell adni. További információ: <https://github.com/lebab/lebab>.

- A rendelkezésre álló transzformációk listájának megjelenítése:

`lebab --help`

- Egy vagy több, vesszővel elválasztott transzformációval történő transzpilálás:

`lebab --transform {{transformation}}`

- Egy fájl transzpileálása a `stdout` címre:

`lebab {{path/to/input_file}}`

- Egy fájl transzpileálása a megadott kimeneti fájlba:

`lebab {{path/to/input_file}} --out-file {{path/to/output_file}}`

- Az összes `.js` fájl helyben történő cseréje a megadott könyvtárban, globusban vagy fájlban:

`lebab --replace {{directory|glob|file}}`
