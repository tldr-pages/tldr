# dvc commit

> A projektben lévő DVC-követésű fájlok változásainak rögzítése. További információ: <https://dvc.org/doc/command-reference/commit>.

- Változások átvétele az összes DVC által követett fájlban és könyvtárban:

`dvc commit`

- Változások rögzítése egy megadott DVC-követésű célponthoz:

`dvc commit {{target}}`

- Egy könyvtárban lévő összes DVC-követett fájl rekurzív rögzítése:

`dvc commit --recursive {{path/to/directory}}`
