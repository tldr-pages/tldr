# mdfind

> Egy adott lekérdezésnek megfelelő fájlok listázása. További információ: <https://ss64.com/osx/mdfind.html>.

- Egy fájl keresése a neve alapján:

`mdfind -name {{file}}`

- Fájl keresése a tartalma alapján:

`mdfind "{{query}}"`

- Egy adott könyvtárban található, egy karakterláncot tartalmazó fájl keresése:

`mdfind -onlyin {{directory}} "{{query}}"`
