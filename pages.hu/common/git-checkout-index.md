# git checkout-index

> Fájlok másolása az indexből a munkafába. További információ: <https://git-scm.com/docs/git-checkout-index>.

- Visszaállítja az utolsó commit óta törölt fájlokat:

`git checkout-index --all`

- A legutóbbi commit óta törölt vagy módosított fájlok visszaállítása:

`git checkout-index --all --force`

- Az utolsó commit óta módosított fájlok visszaállítása, figyelmen kívül hagyva a törölt fájlokat:

`git checkout-index --all --force --no-create`

- A teljes fa másolatának exportálása az utolsó commit időpontjában a megadott könyvtárba (a záróvessző fontos):

`git checkout-index --all --force --prefix={{path/to/export_directory/}}`
