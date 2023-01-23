# cpio

> Fájlok másolása archívumokba és archívumokból. Támogatja a következő archívumformátumokat: cpio egyéni bináris, régi ASCII, új ASCII, crc, HPUX bináris, HPUX régi ASCII, régi tar és POSIX.1 tar. További információ: https: [//www.gnu.org/software/cpio](https://www.gnu.org/software/cpio).

- Fájlnevek listájának átvétele a standard bemenetről, és \[o\]ndja őket egy archívumba a cpio bináris formátumában:

`echo "{{file1}} {{file2}} {{file3}}" | cpio -o > {{archive.cpio}}`

- Egy könyvtárban lévő összes fájl és könyvtár másolása és hozzáadása \[o\]nto egy archívumhoz, \[v\]erbose módban:

`find {{path/to/directory}} | cpio -ov > {{archive.cpio}}`

- P\[i\]ckolja az összes fájlt egy archívumból, szükség esetén \[d\]irectories-t generálva, \[v\]erbose módban:

`cpio -idv < {{archive.cpio}}`
