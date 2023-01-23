# git stage

> Fájlok tartalmának hozzáadása az előkészítő területhez. A `git add` szinonimája. További információ: <https://git-scm.com/docs/git-stage>.

- Fájl hozzáadása az indexhez:

`git stage {{path/to/file}}`

- Az összes (nyomon követett és nem nyomon követett) fájl hozzáadása:

`git stage -A`

- Csak a már nyomon követett fájlok hozzáadása:

`git stage -u`

- Figyelmen kívül hagyott fájlok hozzáadása is:

`git stage -f`

- A fájlok interaktív szakaszolása:

`git stage -p`

- Egy adott fájl egyes részeinek interaktív beállítása:

`git stage -p {{path/to/file}}`

- Egy fájl interaktív szakaszolása:

`git stage -i`
