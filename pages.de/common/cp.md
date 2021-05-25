# cp

> Kopiere Dateien und Verzeichnisse.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/cp>.

- Kopiere eine Datei an einen anderen Ort:

`cp {{pfad/zu/datei}} {{pfad/zu/kopie}}`

- Kopiere eine Datei an einen anderen Ort und behalte den Dateinamen:

`cp {{pfad/zu/datei}} {{pfad/zu/zielverzeichnis}}`

- Kopiere ein Verzeichnis rekursiv (falls der Zielort bereits existiert, wird das Verzeichnis in das Zielverzeichnis kopiert):

`cp -r {{pfad/zu/verzeichnis}} {{pfad/zu/zielverzeichnis}}`

- Kopiere ein Verzeichnis rekursiv und gib alle Dateien aus, während sie kopiert werden:

`cp -vr {{pfad/zu/verzeichnis}} {{pfad/zu/zielverzeichnis}}`

- Kopiere alle Textdateien in einem Verzeichnis und warte auf eine Bestätigung, falls eine Datei überschrieben werden soll:

`cp -i {{/pfad/zu/*.txt}} {{pfad/zu/zielverzeichnis}}`

- Folge symbolischen Links vor dem Kopieren:

`cp -L {{link}} {{pfad/zu/zielverzeichnis}}`
