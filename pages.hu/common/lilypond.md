# lilypond

> Kotta gépelése és/vagy MIDI előállítása fájlból. További információ: <https://lilypond.org>.

- Egy lilypond fájl PDF-be történő összeállítása:

`lilypond {{path/to/file}}`

- Kompilálás a megadott formátumba:

`lilypond --formats={{format_dump}} {{path/to/file}}`

- A megadott fájl lefordítása, a haladás frissítésének elnyomása:

`lilypond -s {{path/to/file}}`

- Kompilálja a megadott fájlt, és adja meg a kimeneti fájlnevet is:

`lilypond --output={{path/to/output_file}} {{path/to/input_file}}`

- A lilypond aktuális verziójának megjelenítése:

`lilypond --version`
