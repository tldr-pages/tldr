# diff

> Fájlok és könyvtárak összehasonlítása. További információ: <https://man7.org/linux/man-pages/man1/diff.1.html>.

- Fájlok összehasonlítása (felsorolja a módosításokat, hogy a `old_file` -ból `new_file` legyen):

`diff {{old_file}} {{new_file}}`

- Fájlok összehasonlítása, a szóközök figyelmen kívül hagyásával:

`diff --ignore-all-space {{old_file}} {{new_file}}`

- Fájlok összehasonlítása, a különbségek egymás melletti megjelenítése:

`diff --side-by-side {{old_file}} {{new_file}}`

- Fájlok összehasonlítása, a különbségek egységes formátumban történő megjelenítése (ahogyan a `git diff` használja):

`diff --unified {{old_file}} {{new_file}}`

- Könyvtárak rekurzív összehasonlítása (megmutatja az eltérő fájlok/könyvtárak neveit, valamint a fájlokban végrehajtott változtatásokat):

`diff --recursive {{old_directory}} {{new_directory}}`

- Könyvtárak összehasonlítása, csak az eltérő fájlok neveinek megjelenítése:

`diff --recursive --brief {{old_directory}} {{new_directory}}`

- A Git számára javítófájl létrehozása két szöveges fájl különbségéből, a nem létező fájlokat üresként kezelve:

`diff --text --unified --new-file {{old_file}} {{new_file}} > {{diff.patch}}`
