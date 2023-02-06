# chown

> A fájlok és könyvtárak felhasználói és csoportos tulajdonjogának módosítása. További információ: <https://www.gnu.org/software/coreutils/chown>.

- Egy fájl/könyvtár tulajdonos felhasználójának módosítása:

`chown {{user}} {{path/to/file_or_directory}}`

- Egy fájl/könyvtár tulajdonos felhasználójának és csoportjának módosítása:

`chown {{user}}:{{group}} {{path/to/file_or_directory}}`

- Egy könyvtár és tartalmának tulajdonosának rekurzív megváltoztatása:

`chown -R {{user}} {{path/to/directory}}`

- Egy szimbolikus hivatkozás tulajdonosának módosítása:

`chown -h {{user}} {{path/to/symlink}}`

- Egy fájl/könyvtár tulajdonosának módosítása egy referenciafájlnak megfelelően:

`chown --reference={{path/to/reference_file}} {{path/to/file_or_directory}}`
