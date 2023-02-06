# tslint

> Beilleszthető linting segédprogram TypeScripthez. További információ: <https://palantir.github.io/tslint>.

- TSLint konfiguráció létrehozása:

`tslint --init`

- Lintelés egy adott fájlkészleten:

`tslint {{filename}}.js {{filename1}}.js`

- A lint problémák kijavítása:

`tslint --fix`

- Lint a projekt gyökerében lévő konfigurációs fájllal:

`tslint --project {{path/to/project_root}}`
