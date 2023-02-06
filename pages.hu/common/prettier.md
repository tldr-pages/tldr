# prettier

> Egy véleményes kódformázó JavaScript, JSON, CSS, YAML és más kódok számára. További információ: <https://prettier.io/>.

- Formázzon meg egy fájlt, és nyomtassa ki az eredményt a `stdout` címre:

`prettier {{path/to/file}}`

- Ellenőrizze, hogy egy adott fájl formázva van-e:

`prettier --check {{path/to/file}}`

- Egy adott konfigurációs fájl futtatása:

`prettier --config {{path/to/config_file}} {{path/to/file}}`

- Formázzon meg egy fájlt vagy könyvtárat, az eredeti helyébe lépve:

`prettier --write {{path/to/file_or_directory}}`

- Fájlok vagy könyvtárak formázása rekurzívan, szimpla idézőjelek és vesszők nélkül:

`prettier --single-quote --trailing-comma {{none}} --write {{path/to/file_or_directory}}`

- JavaScript és TypeScript fájlok rekurzív formázása, az eredeti helyettesítésével:

`prettier --write "**/*.{js,jsx,ts,tsx}"`
