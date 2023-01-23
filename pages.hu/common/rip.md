# rip

> Fájlok vagy könyvtárak eltávolítása a temetőbe küldéssel, lehetővé téve azok helyreállítását. További információ: <https://github.com/nivekuil/rip>.

- Fájlok vagy könyvtárak eltávolítása megadott helyekről, és a temetőbe helyezésük:

`rip {{path/to/file_or_directory}} {{path/to/another/file_or_directory}}`

- Fájlok vagy könyvtárak interaktív eltávolítása, minden eltávolítás előtt felszólítással:

`rip --inspect {{path/to/file_or_directory}} {{path/to/another/file_or_directory}}`

- A temetőben lévő összes olyan fájl és könyvtár listázása, amelyek eredetileg az aktuális könyvtárban voltak:

`rip --seance`

- A temetőben lévő összes fájl és könyvtár végleges törlése:

`rip --decompose`

- A legutóbbi eltávolítás által érintett fájlok és könyvtárak visszahelyezése:

`rip --unbury`

- Minden olyan fájl és könyvtár visszahelyezése, amelyet a `rip --seance` listázott:

`rip --seance --unbury`
