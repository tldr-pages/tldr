# git clean

> A nem követett fájlok eltávolítása a munkafából. További információ: <https://git-scm.com/docs/git-clean>.

- A Git által nem követett fájlok törlése:

`git clean`

- A Git által nem követett fájlok interaktív törlése:

`git clean -i`

- Megmutatja, hogy milyen fájlokat törölne anélkül, hogy ténylegesen törölné őket:

`git clean --dry-run`

- A Git által nem követett fájlok erőszakos törlése:

`git clean -f`

- A Git által nem követett könyvtárak erőszakos törlése:

`git clean -fd`

- Nyomon nem követett fájlok törlése, beleértve a figyelmen kívül hagyott fájlokat a `.gitignore` és a `.git/info/exclude` oldalakon:

`git clean -x`
