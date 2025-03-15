# ls

> Liste den Inhalt eines Verzeichnisses auf.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html>.

- Liste den Inhalt in einer Datei pro Zeile auf:

`ls -1`

- Liste alle Dateien inklusive versteckter Dateien auf:

`ls {{[-a|--all]}}`

- Liste alle Dateien mit einem abschließenden `/` bei Verzeichnis-Namen auf:

`ls {{[-F|--classify]}}`

- Liste alle Dateien mit Berechtigungen, Besitzer, Größe und Änderungsdatum auf:

`ls {{[-la|--all -l]}}`

- Liste alle Dateien mit Dateigröße in für Menschen lesbaren Einheiten (KiB, MiB, GiB):

`ls {{[-lh|-l --human-readable]}}`

- Liste Dateien nach sortiert nach Dateigröße mit größter beginnend auf:

`ls {{-lSR|-lS --recursive}}`

- Liste alle Dateien sortiert nach dem Änderungsdatum mit ältester beginnend auf:

`ls {{[-ltr|-lt --reverse]}}`

- Liste nur Verzeichnisse auf:

`ls {{[-d|--directory]}} */`
