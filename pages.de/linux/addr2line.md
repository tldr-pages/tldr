# addr2line

> Konvertiere Adressen von Binärdateien in Dateinamen und Zeilennummern.
> Weitere Informationen: <https://manned.org/addr2line>.

- Zeige den Dateinamen und die Zeilennummer des Quellcodes von einer Befehlsadresse einer ausführbaren Datei an:

`addr2line {{[-e|--exe]}} {{pfad/zu/binärdatei}} {{adresse}}`

- Zeige den Funktionsnamen, Dateinamen und Zeilennummer an:

`addr2line {{[-e|--exe]}} {{pfad/zu/binärdatei}} {{[-f|--functions]}} {{adresse}}`

- Entmangele den Funktionsnamen für C++ Code:

`addr2line {{[-e|--exe]}} {{pfad/zu/binärdatei}} {{[-f|--functions]}} {{[-C|--demangle]}} {{adresse}}`
