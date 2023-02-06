# shuf

> Véletlenszerű permutációk generálása. További információ: <https://www.gnu.org/software/coreutils/shuf>.

- Véletlenszerűvé teszi a sorok sorrendjét egy fájlban, és kiadja az eredményt:

`shuf {{path/to/file}}`

- Csak az eredmény első 5 bejegyzését adja ki:

`shuf --head-count={{5}} {{path/to/file}}`

- A kimenet kiírása egy másik fájlba:

`shuf {{path/to/input}} --output={{path/to/output}}`

- Generáljon 3 véletlen számot az 1-10-es tartományban (beleértve):

`shuf --head-count={{3}} --input-range={{1-10}} --repeat`
