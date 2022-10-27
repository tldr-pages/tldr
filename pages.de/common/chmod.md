# chmod

> Ändere die Zugriffsberechtigungen einer Datei oder eines Verzeichnisses.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/chmod>.

- Gib dem Besitzer einer Datei ([u]ser) das Recht, sie auszuführen (e[x]ecute):

`chmod u+x {{pfad/zu/datei}}`

- Gib dem Besitzer ([u]ser) Rechte zum Lesen ([r]ead) und Schreiben ([w]rite) einer Datei / einem Verzeichnis:

`chmod u+rw {{pfad/zu/datei_oder_verzeichnis}}`

- Entferne die Ausführrechte (e[x]ecute) der Besitzer[g]ruppe:

`chmod g-x {{pfad/zu/datei}}`

- Gib [a]llen Benutzern Rechte zum Lesen ([r]ead) und Ausführen (e[x]ecute) einer Datei:

`chmod a+rx {{pfad/zu/datei}}`

- Gib anderen ([o]thers) (nicht in der Besitzer[g]ruppe) die gleichen Rechte wie der Besitzer[g]ruppe:

`chmod o=g {{pfad/zu/datei}}`

- Entferne alle Rechte der anderen ([o]thers):

`chmod o= {{pfad/zu/datei}}`

- Ändere Rechte rekursiv, indem der Besitzer[g]ruppe und anderen ([o]thers) die Rechte zum Schreiben ([w]rite) geben werden:

`chmod -R g+w,o+w {{pfad/zu/verzeichnis}}`

- Gib [a]llen Benutzern rekursiv Rechte zum Lesen ([r]ead) von Dateien und Ausführen (e[X]ecute) von Unterverzeichnissen innerhalb eines Verzeichnisses:

`chmod -R a+rX {{pfad/zu/verzeichnis}}`
