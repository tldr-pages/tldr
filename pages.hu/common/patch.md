# patch

> Egy fájl (vagy fájlok) javítása diff fájlokkal. Vegye figyelembe, hogy a diff fájlokat a `diff` paranccsal kell létrehozni. További információ: <https://manned.org/patch>.

- Egy javítás alkalmazása diff fájl segítségével (a diff fájlnak tartalmaznia kell a fájlneveket):

`patch < {{patch.diff}}`

- Egy javítás alkalmazása egy adott fájlra:

`patch {{path/to/file}} < {{patch.diff}}`

- Egy fájl javítása, amelynek eredményét egy másik fájlba írja:

`patch {{path/to/input_file}} -o {{path/to/output_file}} < {{patch.diff}}`

- Folt javítás alkalmazása az aktuális könyvtárra:

`patch -p1 < {{patch.diff}}`

- Egy javítás fordítottjának alkalmazása:

`patch -R < {{patch.diff}}`
