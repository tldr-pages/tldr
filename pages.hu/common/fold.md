# fold

> A bemeneti fájl minden sorát a megadott szélességűre tekeri, és kiírja a szabványos kimenetre. További információ: <https://www.gnu.org/software/coreutils/fold>.

- Minden sor feltekerése az alapértelmezett szélességre (80 karakter):

`fold {{path/to/file}}`

- Minden sor felgöngyölítése "30" szélességűre:

`fold -w30 {{path/to/file}}`

- Minden sort "5" szélességűre tekercsel, és a sort szóközöknél megszakítja (minden szóközzel elválasztott szót új sorba tesz, az 5 karaktert meghaladó hosszúságú szavak fel lesznek tekerve):

`fold -w5 -s {{path/to/file}}`
