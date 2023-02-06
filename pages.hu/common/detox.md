# detox

> Átnevezi a fájlokat, hogy könnyebb legyen velük dolgozni. Eltávolítja a szóközöket és más bosszantó dolgokat, mint például a duplikált aláhúzás karaktereket. További információ: <https://github.com/dharple/detox>.

- Eltávolítja a szóközöket és más nemkívánatos karaktereket a fájl nevéből:

`detox {{path/to/file}}`

- Megmutatja, hogyan nevezné át a detox az összes fájlt egy könyvtárfában:

`detox --dry-run -r {{path/to/directory}}`

- A szóközök és más nemkívánatos karakterek eltávolítása egy könyvtárfa összes fájljából:

`detox -r {{path/to/directory}}`
