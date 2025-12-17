# atom

> Ein plattformübergreifender erweiterbarer Texteditor.
> Erweiterungen werden durch `apm` verwaltet.
> Weitere Informationen: <https://atom.io/>.

- Öffne eine Datei oder ein Verzeichnis:

`atom {{pfad/zu/datei_oder_verzeichnis}}`

- Öffne eine Datei oder ein Verzeichnis in einem neuen Fenster:

`atom {{[-n|--new-window]}} {{pfad/zu/datei_oder_verzeichnis}}`

- Öffne eine Datei oder ein Verzeichnis in einem vorhandenen Fenster:

`atom {{[-a|--add]}} {{pfad/zu/datei_oder_verzeichnis}}`

- Starte Atom im sicheren Modus (Es werden keine zusätzlichen Pakete geladen):

`atom --safe`

- Verhindert, dass sich Atom in den Hintergrund absetzt und hält es mit dem Terminal verbunden:

`atom {{[-f|--foreground]}}`

- Wartet, bis Atom geschlossen wurde, bevor die Eingabeaufforderung wieder aktiv wird (Nützlich als `git commit` Editor):

`atom {{[-w|--wait]}}`
