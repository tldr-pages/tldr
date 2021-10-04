# addr2line

> Konvertiere Adressen von Binaries in Dateinamen und Zeilennummern.
> Mehr Informationen: <https://manned.org/addr2line>.

- Zeige den Dateinamen und die Zeilennummer im Quellcode von einer Anweisungsadresse eines Executables:

`addr2line --exe={{pfad/zum/executable}} {{adresse}}`

- Zeige den Funktionsnamen, Dateinamen und Zeilennummer:

`addr2line --exe={{pfad/zum/executable}} --functions {{adresse}}`

- Entmangele den Funktionsnamen für C++ Code:

`addr2line --exe={{pfad/zum/executable}} --functions --demangle {{adresse}}`
