# cp

> Lopiere Dateien und Ordner.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/cp>.

- Kopiere eine Datei an einem anderen Ort:

`cp {{Pfad/zur/Quelldatei.ext}} {{Pfad/zur/Zieldatei.ext}}`

- Kopiere eine Datei in einen anderen Ordner ohne die Datei umzubenennen:

`cp {{Pfad/zur/Quelldatei.ext}} {{Pfad/zum/Zielordner}}`

- Kopiere die Inhalte eines Ordners rekursiv zu einem anderen Ort (Falls der Zielordner bereits existiert wird der Ordner hinein kopiert):

`cp -r {{Pfad/zum/Quellordner}} {{Pfad/zum/Zielordner}}`

- Kopiere einen Ordner rekursiv im detailierten Modus (listet Dateien auf während die kopiert werden):

`cp -vr {{Pfad/zum/Quellordner}} {{Pfad/zum/Zielordner}}`

- Kopiere text Dateien in einen anderen Ordner im interaktiven Modus (Fragt den Benutzer nache einer Bestätigung vor dem Überschreiben):

`cp -i {{*.txt}} {{Pfad/zum/Zielordner}}`

- Folge symbolische Verlinkunge vor dem kopieren:

`cp -L {{link}} {{Pfad/zum/Zielordner}}`

- Verwende den vollständigen Pfad der Quelldatei und erstellen beim Kopieren alle fehlenden Zwischenverzeichnisse:

`cp --parents {{Quellpfad/zur/Datei}} {{Pfad/zur/ZielDatei}}`
