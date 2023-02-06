# git check-ignore

> Git ignore / exclude (".gitignore") fájlok elemzése és hibakeresése. További információ: <https://git-scm.com/docs/git-check-ignore>.

- Annak ellenőrzése, hogy egy fájl vagy könyvtár figyelmen kívül van-e hagyva:

`git check-ignore {{path/to/file_or_directory}}`

- Annak ellenőrzése, hogy több fájl vagy könyvtár figyelmen kívül van-e hagyva:

`git check-ignore {{path/to/file}} {{path/to/directory}}`

- Használja az elérési utakat, soronként egyet, a `stdin`:

`git check-ignore --stdin < {{path/to/file_list}}`

- Ne ellenőrizze az indexet (hibakeresésre használják, hogy miért követték és miért nem hagyták figyelmen kívül az elérési utakat):

`git check-ignore --no-index {{path/to/files_or_directories}}`

- Adja meg az egyes elérési utak megfelelő mintájának részleteit:

`git check-ignore --verbose {{path/to/files_or_directories}}`
