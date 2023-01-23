# trash

> CLI a szemetes / újrahasznosító kuka kezeléséhez. További információ: <https://github.com/andreafrancia/trash-cli>.

- Egy fájl törlése és a szemetesbe küldése:

`trash {{path/to/file}}`

- A szemetesben lévő összes fájl listázása:

`trash-list`

- Egy fájl interaktív visszaállítása a szemetesből:

`trash-restore`

- A szemetes kiürítése:

`trash-empty`

- A szemetesben lévő összes, 10 napnál régebbi fájl végleges törlése:

`trash-empty {{10}}`

- A szemetesben lévő összes olyan fájl eltávolítása, amely megfelel egy adott blob-mintának:

`trash-rm "{{*.o}}"`

- Az összes olyan fájl eltávolítása, amelyeknek meghatározott eredeti helye van:

`trash-rm {{/path/to/file_or_directory}}`
