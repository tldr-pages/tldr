# gcc

> Präprozessiert und kompiliert C und C++ Quellcodedateien und linkt diese anschließend zusammen.
> Weitere Informationen: <https://gcc.gnu.org>.

- Kompiliere mehrere Quellcodedateien zu einer ausführbaren Datei:

`gcc {{pfad/zu/datei1.c}} {{pfad/zu/datei2.c}} --output {{pfad/zu/binärdatei}}`

- Erlaube Warnungen und debug-Symbole in der Ausgabedatei:

`gcc {{pfad/zu/datei.c}} -Wall -Og --output {{pfad/zu/binärdatei}}`

- Inkludiere Bibliotheken aus anderen Verzeichnissen:

`gcc {{pfad/zu/datei.c}} --output {{pfad/zu/binärdatei}} -I{{pfad/zu/headerdatei}} -L{{pfad/zu/bibliothek1}} -l{{pfad/zu/bibliothek2}}`

- Kompiliere Quellcodedateien zu Assemblerinstruktionen:

`gcc -S {{pfad/zu/datei.c}}`

- Kompiliere eine oder mehrere Quellcodedateien ohne diese zu linken:

`gcc -c {{pfad/zu/datei.c}}`
