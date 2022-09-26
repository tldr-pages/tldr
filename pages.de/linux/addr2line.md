# addr2line

> Konvertiere Adressen von Binärdateien in Dateinamen und Zeilennummern.
> Weitere Informationen: <https://manned.org/addr2line>.

- Zeige den Dateinamen und die Zeilennummer des Quellcodes von einer Befehlssadresse einer ausführbaren Datei an:

`addr2line --exe={{pfad/zur/ausführbaren_datei}} {{adresse}}`

- Zeige den Funktionsnamen, Dateinamen und Zeilennummer an:

`addr2line --exe={{pfad/zum/executable}} --functions {{adresse}}`

- Entmangele den Funktionsnamen für C++ Code:

`addr2line --exe={{pfad/zum/executable}} --functions --demangle {{adresse}}`
