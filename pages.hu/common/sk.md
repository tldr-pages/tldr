# sk

> Rust nyelven írt Fuzzy finder. Hasonló a `fzf`. További információ: [https://github.com/lotabout/skim.](https://github.com/lotabout/skim)

- A megadott könyvtárban lévő összes fájl lefutásának elindítása:

`find {{path/to/directory}} -type f | sk`

- Skim indítása a futó folyamatokra:

`ps aux | sk`

- Skim indítása egy megadott lekérdezéssel:

`sk --query "{{query}}"`

- Több fájl kiválasztása a `Shift + Tab` segítségével és írása egy fájlba:

`find {{path/to/directory}} -type f | sk --multi > {{path/to/file}}`
