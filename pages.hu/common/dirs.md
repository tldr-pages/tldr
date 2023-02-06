# dirs

> Megjeleníti vagy manipulálja a könyvtárhalmazt. A könyvtárhalmaz a legutóbb meglátogatott könyvtárak listája, amely a `pushd` és a `popd` parancsokkal manipulálható. További információ: <https://www.gnu.org/software/bash/manual/bash.html#Directory-Stack-Builtins>.

- Megjeleníti a könyvtárhalmazt úgy, hogy az egyes bejegyzések között szóköz van:

`dirs`

- Megjeleníti a könyvtárhalmazt soronként egy bejegyzéssel:

`dirs -p`

- Csak az n-edik bejegyzést jeleníti meg a könyvtárhalmazban, 0-tól kezdve:

`dirs +{{N}}`

- A könyvtárhalmaz törlése:

`dirs -c`
