# cfdisk

> Ein Programm zur Verwaltung von Partitionstabellen mittels einer Curses-basierten UI.
> Weitere Informationen: <https://manned.org/cfdisk>.

- Öffne das Partitionierungsinterface für eine bestimmte Festplatte:

`cfdisk {{/dev/sdX}}`

- Erzeuge und bearbeite eine neue Partitionierungstabelle für eine bestimmte Festplatte:

`cfdisk {{[-z|--zero]}} {{/dev/sdX}}`
