# dot_clean

> .\_\* fájlok egyesítése a megfelelő natív fájlokkal. További információ: <https://ss64.com/osx/dot_clean.html>.

- Az összes `._*` fájl rekurzív egyesítése:

`dot_clean {{path/to/directory}}`

- Ne egyesítse rekurzívan az összes `._*` fájlt egy könyvtárban (flat merge):

`dot_clean -f {{path/to/directory}}`

- Az összes `._*` fájl egyesítése és törlése:

`dot_clean -m {{path/to/directory}}`

- Csak akkor törölje a `._*` fájlokat, ha van megfelelő natív fájl:

`dot_clean -n {{path/to/directory}}`

- Kövesse a szimlinkeket:

`dot_clean -s {{path/to/directory}}`

- Szöveges kimenet nyomtatása:

`dot_clean -v {{path/to/directory}}`
