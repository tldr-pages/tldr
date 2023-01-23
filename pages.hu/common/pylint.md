# pylint

> Egy Python kódinterflektor. További információ: <https://pylint.pycqa.org/en/latest/>.

- A lint hibák megjelenítése egy fájlban:

`pylint {{path/to/file.py}}`

- Lint egy fájl és egy konfigurációs fájl használata (általában a `pylintrc`):

`pylint --rcfile {{path/to/pylintrc}} {{path/to/file.py}}`

- Lint egy fájl és egy adott hibakód letiltása:

`pylint --disable {{C,W,no-error,design}} {{path/to/file}}`
