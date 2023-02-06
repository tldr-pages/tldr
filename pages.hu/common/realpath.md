# realpath

> Egy fájl vagy könyvtár felbontott abszolút elérési útjának megjelenítése. További információ: <https://www.gnu.org/software/coreutils/realpath>.

- Egy fájl vagy könyvtár abszolút elérési útjának megjelenítése:

`realpath {{path/to/file_or_directory}}`

- Az összes elérési útvonal-összetevő létezésének megkövetelése:

`realpath --canonicalize-existing {{path/to/file_or_directory}}`

- Feloldja a ".." komponenseket a szimlinkek előtt:

`realpath --logical {{path/to/file_or_directory}}`

- Symlink kiterjesztés letiltása:

`realpath --no-symlinks {{path/to/file_or_directory}}`

- Hibaüzenetek elnyomása:

`realpath --quiet {{path/to/file_or_directory}}`
