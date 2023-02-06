# czkawka-cli

> A `czkawka` parancssoros verziója egy multifunkcionális alkalmazás, amely duplikátumokat, üres mappákat, hasonló képeket és még sok mást keres. További információ: <https://github.com/qarmin/czkawka>.

- Listázza ki a duplikált vagy hasonló fájlokat bizonyos könyvtárakban:

`czkawka-cli {{dup|image}} --directories {{path/to/directory1 path/to/directory2 ...}}`

- Duplikált fájlok keresése és törlése meghatározott könyvtárakban (alapértelmezett: `NONE`):

`czkawka-cli dup --directories {{path/to/directory1 path/to/directory2 ...}} --delete-method {{AEN|AEO|ON|OO|HARD|NONE}}`
