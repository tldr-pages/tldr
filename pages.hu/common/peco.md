# peco

> Interaktív szűrőeszköz. További információ: <https://github.com/peco/peco>.

- A peco elindítása a megadott könyvtárban lévő összes fájlon:

`find {{path/to/directory}} -type f | peco`

- A peco elindítása a futó folyamatokra:

`ps aux | peco`

- A peco elindítása egy megadott lekérdezéssel:

`peco --query "{{query}}"`
