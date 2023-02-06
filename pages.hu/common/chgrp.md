# chgrp

> A fájlok és könyvtárak csoportos tulajdonjogának módosítása. További információ: <https://www.gnu.org/software/coreutils/chgrp>.

- Egy fájl/könyvtár tulajdonos csoportjának megváltoztatása:

`chgrp {{group}} {{path/to/file_or_directory}}`

- Egy könyvtár és tartalmának tulajdonosi csoportjának rekurzív megváltoztatása:

`chgrp -R {{group}} {{path/to/directory}}`

- Egy szimbolikus hivatkozás tulajdonoscsoportjának módosítása:

`chgrp -h {{group}} {{path/to/symlink}}`

- Egy fájl/könyvtár tulajdonosi csoportjának módosítása egy referenciafájlnak megfelelően:

`chgrp --reference={{path/to/reference_file}} {{path/to/file_or_directory}}`
