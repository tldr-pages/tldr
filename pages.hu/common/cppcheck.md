# cppcheck

> Statikus elemző eszköz C/C++ kódhoz. A szintaktikai hibák helyett azokra a hibatípusokra összpontosít, amelyeket a fordítóprogramok általában nem észlelnek. További információ: <http://cppcheck.sourceforge.net>.

- Rekurzívan ellenőrzi az aktuális könyvtárat, a képernyőn mutatja a haladást és naplózza a hibaüzeneteket egy fájlba:

`cppcheck . 2> cppcheck.log`

- Rekurzívan ellenőriz egy adott könyvtárat, és nem ír ki előrehaladási üzeneteket:

`cppcheck --quiet {{path/to/directory}}`

- Egy adott fájl ellenőrzése, megadva, hogy milyen teszteket hajtson végre (alapértelmezés szerint csak a hibák jelennek meg):

`cppcheck --enable={{error|warning|style|performance|portability|information|all}} {{path/to/file.cpp}}`

- A rendelkezésre álló tesztek listázása:

`cppcheck --errorlist`

- Egy adott fájl ellenőrzése, bizonyos tesztek figyelmen kívül hagyásával:

`cppcheck --suppress={{test_id1}} --suppress={{test_id2}} {{path/to/file.cpp}}`

- Az aktuális könyvtár ellenőrzése, megadva a könyvtáron kívül található include fájlok (pl. külső könyvtárak) elérési útvonalát:

`cppcheck -I {{include/directory_1}} -I {{include/directory_2}} .`

- Microsoft Visual Studio projekt (`*.vcxproj`) vagy megoldás (`*.sln`) ellenőrzése:

`cppcheck --project={{path/to/project.sln}}`
