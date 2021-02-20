# atom

> Ein plattformübergreifender erweiterbarer Texteditor.
> Erweiterungen werden durch `apm` verwaltet.
> Weitere Information: <https://atom.io/>.

- Öffne eine Datei oder ein Verzeichnis:

`atom {{pfad/zu/datei_oder_verzeichnis}}`

- Öffne eine Datei oder ein Verzeichnis in einem neuen Fenster:

`atom -n {{pfad/zu/datei_oder_verzeichnis}}`

- Öffne eine Datei oder ein Verzeichnis in einem vorhendenen Fenster:

`atom --add {{pfad/zu/datei_oder_verzeichnis}}`

- Stare Atom im sicheren Modus (Es werden keine zusätzlichen Pakete geladen):

`atom --safe`

- Verhindert, dass sich Atom in den Hintergrund absetzt und hält es verbunden mit den Terminal:

`atom --foreground`

- Wartet, bis Atom geschlossen wurde, bevor die Eingabeaufforderung wieder aktiv wird (Nützlich als git commit Editor):

`atom --wait`
