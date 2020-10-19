# gcc

> Präprozessiert und kompiliert C und C++ Quellcodedateien und linkt diese anschließend zusammen.
> Mehr Informationen: <https://gcc.gnu.org>.

- Kompiliert mehrere Quellcodedateien zu einer ausführbaren Datei:

`gcc {{Quelldatei1.c}} {{Quelldatei2.c}} -o {{Ausgabebinärdatei}}`

- Erlaubt Warnungen und debug-Symbole in der Ausgabedatei:

`gcc {{source.c}} -Wall -Og -o {{Ausgabebinärdatei}}`

- Inkludiert Bibliotheken aus anderen Ordnern:

`gcc {{Quelldatei.c}} -o {{Ausgabebinärdatei}} -I{{Pfad_zu_Headerdatei}} -L{{Pfad_zu_Bibliothek1}} -l{{Pfad_zu_Bibliothek2}}`

- Kompiliert Quellcodedateien zu Assemblerinstruktionen:

`gcc -S {{Quelldatei.c}}`

- Kompiliert Quellcodedatei/-en ohne diese zu linken:

`gcc -c {{Quelldatei.c}}`
