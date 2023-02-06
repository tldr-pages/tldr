# dirname

> Kiszámítja egy adott fájl vagy könyvtár elérési útvonalának szülői könyvtárát. További információ: <https://www.gnu.org/software/coreutils/dirname>.

- Egy adott elérési útvonal szülői könyvtárának kiszámítása:

`dirname {{path/to/file_or_directory}}`

- Több elérési útvonal szülői könyvtárának kiszámítása:

`dirname {{path/to/file_a}} {{path/to/directory_b}}`

- A kimenetet újsor helyett NUL karakterrel határolja (hasznos a `xargs` címmel való kombináláskor):

`dirname --zero {{path/to/directory_a}} {{path/to/file_b}}`
