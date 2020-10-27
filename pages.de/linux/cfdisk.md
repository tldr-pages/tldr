# cfdisk

> Ein Programm zur Verwaltung von Partitionstabellen mittels einer Curses-basierten UI.
> Weitere Informationen: <https://linux.die.net/man/8/cfdisk>

- Das Partitionierungsinterface für die Festplatte /dev/sda öffnen:

`cfdisk {{/dev/sda}}`

- Eine neue Partitionierungstabelle für die Festplatte /dev/sda erzeugen und bearbeiten:

`cfdisk --zero {{/dev/sda}}`
