# cp

> Kopiere Dateien und Verzeichnisse.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/cp>.

- Kopiere eine Datei an einen anderen Ort:

`cp {{pfad/zu/ausgangs_datei.ext}} {{pfad/zu/ziel_datei.ext}}`

- Kopiere eine Datei in ein anderes Verzeichnis und behalte den Dateinamen bei:

`cp {{pfad/zu/ausgang_datei.ext}} {{pfad/zu/ziel_verzeichnis}}`

- Kopiere die Inhalte eines Verzeichnisses rekursiv zu einem neuen Ort (wenn das Ziel existiert, wird das Verzeichnis ins bestehende Ziel Verzeichnis kopiert):

`cp -r {{pfad/zu/ausgangs_verzeichnis}} {{pfad/zu/ziel_verzeichnis}}`

- Kopiere ein Verzeichnis rekursiv im ausführlichen Modus (zeigt die Dateien die kopiert werden):

`cp -vr {{pfad/zu/ausgangs_verzeichnis}} {{pfad/zu/ziel_verzeichnis}}`

- Kopiere text Dateien zu einem anderen Ort im interaktiven Modus (fragt die Nutzer:in bevor eine Datei überschrieben wird):

`cp -i {{*.txt}} {{pfad/zu/ziel_verzeichnis}}`

- Folge symbolischen Verzeichnislinks vorm Kopieren:

`cp -L {{link}} {{pfad/zu/ziel_verzeichnis}}`

- Benutze den vollen Pfad der Ausgangsdateien und erstelle alle fehlenden Verzeichnisse beim Kopieren:

`cp --parents {{quelle/pfad/zu/datei}} {{pfad/zu/ziel_datei}}`
