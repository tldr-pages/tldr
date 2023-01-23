# rsync

> Fájlok átvitele egy távoli gépre vagy egy távoli gépről (nem két távoli gép között). Egyetlen fájl vagy egy mintának megfelelő több fájl átvitele. További információ: <https://manned.org/rsync>.

- Fájlok átvitele a helyi állomásról a távoli állomásra:

`rsync {{path/to/local_file}} {{remote_host}}:{{path/to/remote_directory}}`

- Fájl átvitele távoli állomásról a helyi állomásra:

`rsync {{remote_host}}:{{path/to/remote_file}} {{path/to/local_directory}}`

- Fájl átvitele \[a\]rchive (az attribútumok megőrzése érdekében) és tömörített (\[z\]ipped) módban, \[v\]erbose és \[h\]uman-readable \[P\]rogress:

`rsync -azvhP {{path/to/local_file}} {{remote_host}}:{{path/to/remote_directory}}`

- Egy könyvtár és annak összes gyermekkönyvtárának átvitele távoli helyről helyi helyre:

`rsync -r {{remote_host}}:{{path/to/remote_directory}} {{path/to/local_directory}}`

- A könyvtár tartalmának (de nem magának a könyvtárnak) az átvitele egy távoli könyvtárból a helyi könyvtárba:

`rsync -r {{remote_host}}:{{path/to/remote_directory}}/ {{path/to/local_directory}}`

- Egy könyvtár \[r\]ekurzív módon, \[a\]rchive-ban történő átvitele az attribútumok megőrzése érdekében, a benne lévő soft\[l\]inkek feloldása, és a már átvitt fájlok figyelmen kívül hagyása \[u\]n\]gy újabbak kivételével:

`rsync -rauL {{remote_host}}:{{path/to/remote_directory}} {{path/to/local_directory}}`

- Fájl átvitele SSH-n keresztül, és a helyben nem létező távoli fájlok törlése:

`rsync -e ssh --delete {{remote_host}}:{{path/to/remote_file}} {{path/to/local_file}}`

- Fájl átvitele SSH-n keresztül az alapértelmezettől eltérő portot használva, és globális előrehaladás megjelenítése:

`rsync -e 'ssh -p {{port}}' --info=progress2 {{remote_host}}:{{path/to/remote_file}} {{path/to/local_file}}`
