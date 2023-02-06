# fzf

> Parancssori fuzzy kereső. Hasonló a `sk`-hoz. További információ: [https://github.com/junegunn/fzf.](https://github.com/junegunn/fzf)

- Az fzf elindítása a megadott könyvtárban lévő összes fájlon:

`find {{path/to/directory}} -type f | fzf`

- Az fzf elindítása a futó folyamatokra:

`ps aux | fzf`

- Több fájl kijelölése a `Shift + Tab` segítségével és írása egy fájlba:

`find {{path/to/directory}} -type f | fzf --multi > {{path/to/file}}`

- Az fzf elindítása egy megadott lekérdezéssel:

`fzf --query "{{query}}"`

- Az fzf elindítása a core-ral kezdődő és go, rb vagy py végű bejegyzéseken:

`fzf --query "^core go$ | rb$ | py$"`

- Az fzf indítása olyan bejegyzésekre, amelyek nem egyeznek pyc-vel és pontosan travis-szel:

`fzf --query "!pyc 'travis"`
