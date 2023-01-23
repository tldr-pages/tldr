# cp

> Fájlok és könyvtárak másolása. További információ: <https://www.gnu.org/software/coreutils/cp>.

- Fájl másolása egy másik helyre:

`cp {{path/to/source_file.ext}} {{path/to/target_file.ext}}`

- Egy fájl másolása egy másik könyvtárba, a fájlnév megtartásával:

`cp {{path/to/source_file.ext}} {{path/to/target_parent_directory}}`

- Egy könyvtár tartalmának rekurzív másolása egy másik helyre (ha a célállomás létezik, a könyvtár belemásolódik):

`cp -r {{path/to/source_directory}} {{path/to/target_directory}}`

- Egy könyvtár rekurzív másolása, bőbeszédű üzemmódban (a fájlok másolás közbeni megjelenítése):

`cp -vr {{path/to/source_directory}} {{path/to/target_directory}}`

- Szöveges fájlok másolása egy másik helyre, interaktív módban (a felülírás előtt megkérdezi a felhasználót):

`cp -i {{*.txt}} {{path/to/target_directory}}`

- Szimbolikus hivatkozások követése másolás előtt:

`cp -L {{link}} {{path/to/target_directory}}`

- A forrásfájlok teljes elérési útját használja, másoláskor létrehozva a hiányzó közbenső könyvtárakat:

`cp --parents {{source/path/to/file}} {{path/to/target_file}}`
