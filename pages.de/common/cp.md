# cp

> Kopieren von Dateien und Ordnern.

- Kopieren einer Datei an einen anderen Ort:

`cp {{pfad/zur/datei.ext}} {{pfad/zur/kopie.ext}}`

- Kopieren einer Datei an einen anderen Ort mit gleichem Dateinamen:

`cp {{pfad/zur/datei.ext}} {{pfad/zum/ziel_ort}}`

- Rekursives Kopieren aller Ordnerinhalte an einen anderen Ort (falls der Zielort bereits existiert, wird der Ordner in den Zielordner kopiert):

`cp -r {{pfad/zum/ordner}} {{pfad/zum/ziel_ort}}`

- Rekursives Kopieren eines Ordners im ausführlichen Modus (Dateien werden aufgelistet, während sie kopiert werden):

`cp -vr {{pfad/zum/ordner}} {{pfad/zum/ziel_ort}}`

- Kopieren von Textdateien an einen anderen Ort im interaktiven Modus (Fordert den Nutzer vor dem Überschreiben zur Bestätigung auf):

`cp -i {{*.txt}} {{pfad/zum/ziel_ort}}`
