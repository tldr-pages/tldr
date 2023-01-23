# fgrep

> Fix karakterláncok egyeztetése fájlokban. A `grep -F` megfelelője. További információ: <https://www.gnu.org/software/grep/manual/grep.html>.

- Pontos karakterlánc keresése egy fájlban:

`fgrep {{search_string}} {{path/to/file}}`

- Csak olyan sorok keresése, amelyek teljes egészében megegyeznek a fájlokban:

`fgrep -x {{path/to/file1}} {{path/to/file2}}`

- Megszámolja a megadott karakterláncnak megfelelő sorok számát egy fájlban:

`fgrep -c {{search_string}} {{path/to/file}}`

- Megjeleníti a fájlban a sorszámot a megfelelő sorral együtt:

`fgrep -n {{search_string}} {{path/to/file}}`

- Az összes sor megjelenítése a keresett karakterláncot tartalmazó sorok kivételével:

`fgrep -v {{search_string}} {{path/to/file}}`

- Azoknak a fájlneveknek a megjelenítése, amelyek tartalma legalább egyszer megegyezik a keresési karakterlánccal:

`fgrep -l {{search_string}} {{path/to/file1}} {{path/to/file2}}`
