# yapf

> Python style guide checker. További információ: <https://github.com/google/yapf>.

- Megjelenít egy diff-et a végrehajtandó változtatásokról, anélkül, hogy elvégezné azokat (dry-run):

`yapf --diff {{path/to/file}}`

- A fájl helyben történő formázása és a változtatások diff-jének megjelenítése:

`yapf --diff --in-place {{path/to/file}}`

- Egy könyvtárban lévő összes Python-fájl rekurzív formázása egyidejűleg:

`yapf --recursive --in-place --style {{pep8}} --parallel {{path/to/directory}}`
