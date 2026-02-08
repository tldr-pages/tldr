# git blame

> Zeige den Commit-Hash und den letzten Autor jeder Zeile einer Datei.
> Weitere Informationen: <https://git-scm.com/docs/git-blame>.

- Gib die Commit-Hashes und den Autor jeder Zeile einer Datei aus:

`git blame {{pfad/zu/datei}}`

- Gib die E-Mail des Autors statt des Namens aus:

`git blame {{[-e|--show-email]}} {{pfad/zu/datei}}`

- Gib die Commit-Hashes und den Autor jeder Zeile einer Datei zu einem bestimmten Commit aus:

`git blame {{commit}} {{pfad/zu/datei}}`

- Gib die Commit-Hashes und den Autor jeder Zeile einer Datei vor einem bestimmten Commit aus:

`git blame {{commit}}~ {{pfad/zu/datei}}`

- Gib die Commit-Hashes und den Autor ab einer bestimmten Zeile aus:

`git blame -L {{123}} {{pfad/zu/datei}}`

- Annotiere einen bestimmten Zeilenbereich einer Datei:

`git blame -L {{startzeile}},{{endzeile}} {{pfad/zu/datei}}`

- Annotiere 10 Zeilen einer Datei ab der ersten Zeile, die einem bestimmten Text entspricht:

`git blame -L '/{{text}}/',+10 {{pfad/zu/datei}}`

- Annotiere eine Datei unter Ignorierung von Leerzeichen und Zeilenverschiebungen:

`git blame -w -C -C -C {{pfad/zu/datei}}`
