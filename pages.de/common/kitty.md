# kitty

> Ein schneller, funktionsreicher, auf der GPU basierender Terminal-Emulator.
> Weitere Informationen: <https://sw.kovidgoyal.net/kitty/>.

- Öffne ein neues Terminal:

`kitty`

- Öffne ein Terminal mit einem festgelegten Titel für das Fenster:

`kitty --title "{{Titel}}"`

- Starte die integrierte Theme-Auswahl:

`kitty +kitten themes`

- Zeige ein Bild im Terminal an:

`kitty +kitten icat {{Pfad/zum/Bild}}`

- Kopiere den Inhalt von `stdin` in die Zwischenablage:

`echo {{Beispiel}} | kitty +kitten clipboard`
