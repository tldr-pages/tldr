# kitty

> Ein schneller, funktionsreicher, auf der GPU basierender Terminal-Emulator.
> Weitere Informationen: <https://sw.kovidgoyal.net/kitty/>.

- Öffne ein neues Terminal:

`kitty`

- Öffne ein Terminal mit einem festgelegten Titel für das Fenster:

`kitty --title "{{Titel}}"`

- Starte die integrierte Farbschema-Auswahl:

`kitty +kitten themes`

- Zeige ein Bild im Terminal an:

`kitty +kitten icat {{pfad/zum/bild}}`

- Kopiere den Inhalt von `stdin` in die Zwischenablage:

`echo {{Beispiel}} | kitty +kitten clipboard`
