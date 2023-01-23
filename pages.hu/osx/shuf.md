# shuf

> Véletlenszerű permutációk generálása. További információ: <https://www.unix.com/man-page/linux/1/shuf/>.

- Véletlenszerűvé teszi a sorok sorrendjét egy fájlban, és kiadja az eredményt:

`shuf {{filename}}`

- Csak az eredmény első 5 bejegyzését adja ki:

`shuf --head-count={{5}} {{filename}}`

- Kimenet kiírása egy másik fájlba:

`shuf {{filename}} --output={{output_filename}}`

- Véletlen számok generálása az 1-10-es tartományban:

`shuf --input-range={{1-10}}`
