# rm

> Lösche Dateien oder Verzeichnisse.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/rm>.

- Lösche Dateien an beliebigen Speicherorten:

`rm {{pfad/zu/datei}} {{pfad/zu/anderer/datei}}`

- Lösche ein Verzeichnis und alle seine Unterverzeichnisse rekursiv:

`rm -r {{pfad/zu/verzeichnis}}`

- Erzwinge das Löschen eines Verzeichnisses, ohne Eingabeaufforderung zur Bestätigung oder Anzeigen von Fehlermeldungen:

`rm -rf {{pfad/zu/verzeichnis}}`

- Lösche mehrere Dateien mit Eingabeaufforderung zur Bestätigung für jede Datei:

`rm -i {{pfad/zu/datei1 pfad/zu/datei2 ...}}`

- Liste jede Datei auf, wenn sie gelöscht wird:

`rm -v {{pfad/zu/verzeichnis/*}}`
