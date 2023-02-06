# git submodule

> Ellenőrzi, frissíti és kezeli az almodulokat. További információ: <https://git-scm.com/docs/git-submodule>.

- Telepíti egy tároló megadott almoduljait:

`git submodule update --init --recursive`

- Egy Git-tárhely hozzáadása almodulként:

`git submodule add {{repository_url}}`

- Egy Git-tárhely hozzáadása almodulként a megadott könyvtárban:

`git submodule add {{repository_url}} {{path/to/directory}}`

- Minden almodul frissítése a legutóbbi commitra:

`git submodule foreach git pull`
