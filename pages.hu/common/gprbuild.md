# gprbuild

> Magas szintű építőeszköz Ada és más nyelveken (C/C++/Fortran) írt projektekhez. További információ: <https://docs.adacore.com/gprbuild-docs/html/gprbuild_ug.html>.

- Egy projekt építése (feltételezve, hogy csak egy `*.gpr` fájl létezik az aktuális könyvtárban):

`gprbuild`

- Egy adott \[P\]rojektfájl építése:

`gprbuild -P{{project_name}}`

- A build munkaterület megtisztítása:

`gprclean`

- Kompilált bináris állományok telepítése:

`gprinstall --prefix {{path/to/installation/dir}}`
