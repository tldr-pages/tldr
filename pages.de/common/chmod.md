# chmod

> Ändere die Zugriffsberechtigungen einer Datei oder eines Verzeichnisses.

- Gib dem Benutzer ([u]ser), der Eigentümer einer Datei ist, das Recht, diese zu auszuführen (e[x]ecute):

`chmod u+x {{file}}`

- Gib dem Benutzer ([u]ser) Rechte zum lesen ([r]ead) und schreiben ([w]rite) an einer Datei / einem Verzeichnis:

`chmod u+rw {{file_or_directory}}`

- Entferne ausführbare (e[x]ecutable) Rechte aus der [g]ruppe:

`chmod g-x {{file}}`

- Gib [a]llen Benutzern Rechte zum lesen ([r]ead) und ausführen (e[x]ecute) an einer Datei:

`chmod a+rx {{file}}`

- Gib anderen ([o]thers) (nicht in der Gruppe des Dateieigentümers) die gleichen Rechte wie der [g]ruppe:

`chmod o=g {{file}}`

- Entferne alle Rechtr der Anderen ([o]thers):

`chmod o= {{file}}`

- Ändere Genehmigungen rekursiv, indem Sie  [g]ruppe and Anderen ([o]thers) die Erlaubniss zum schreiben ([w]rite) geben:

`chmod -R g+w,o+w {{directory}}`
