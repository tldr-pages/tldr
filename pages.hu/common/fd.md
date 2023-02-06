# fd

> A `find` alternatívája. Célja, hogy gyorsabb és könnyebben használható legyen, mint a `find`. További információ: <https://github.com/sharkdp/fd>.

- Rekurzívan keres egy adott mintának megfelelő fájlokat az aktuális könyvtárban:

`fd "{{string|regex}}"`

- A `foo` kezdőbetűvel kezdődő fájlok keresése:

`fd "^foo"`

- Meghatározott kiterjesztésű fájlok keresése:

`fd --extension txt`

- Fájlok keresése egy adott könyvtárban:

`fd "{{string|regex}}" {{path/to/directory}}`

- Figyelmen kívül hagyott és rejtett fájlok bevonása a keresésbe:

`fd --hidden --no-ignore "{{string|regex}}"`

- Parancs végrehajtása minden egyes visszaküldött keresési eredményen:

`fd "{{string|regex}}" --exec {{command}}`
