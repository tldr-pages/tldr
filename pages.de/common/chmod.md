# chmod

> Ändere die Zugriffsberechtigungen einer Datei oder eines Verzeichnisses.

- Gib dem Benutzer ([u]ser), der Eigentümer einer Datei ist, das Recht, diese zu auszuführen (e[x]ecute):

`chmod u+x {{datei}}`

- Gib dem Benutzer ([u]ser) Rechte zum lesen ([r]ead) und schreiben ([w]rite) an einer Datei / einem Verzeichnis:

`chmod u+rw {{datei_oder_verzeichnis}}`

- Entferne ausführbare (e[x]ecutable) Rechte aus der [g]ruppe:

`chmod g-x {{datei}}`

- Gibt [a]llen Benutzern Rechte zum lesen ([r]ead) und ausführen (e[x]ecute) an einer Datei:

`chmod a+rx {{datei}}`

- Gibt anderen ([o]thers) (nicht in der Gruppe des Dateieigentümers) die gleichen Rechte wie der [g]ruppe:

`chmod o=g {{datei}}`

- Entfernt alle Rechte der Anderen ([o]thers):

`chmod o= {{datei}}`

- Ändert Genehmigungen rekursiv, indem Sie [g]ruppe und Anderen ([o]thers) die Erlaubniss zum schreiben ([w]rite) geben:

`chmod -R g+w,o+w {{verzeichnis}}`
