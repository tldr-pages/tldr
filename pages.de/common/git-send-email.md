# git send-email

> Sende eine Menge von Patches als E-Mail. Patches können als Dateien, Ordner oder Liste von Revisionen spezifiziert werden.
> Weitere Informationen: <https://git-scm.com/docs/git-send-email>.

- Sende den letzten Commit des aktuellen Branches:

`git send-email -1`

- Sende einen spezifischen Commit:

`git send-email -1 {{commit}}`

- Sende die letzten (z.B. 10) Commits des aktuellen Branches:

`git send-email {{-10}}`

- Editiere eine E-Mail mit einer Reihe von Patches im Standardmailclienten:

`git send-email -{{anzahl_an_commits}} --compose`

- Bearbeite den E-Mail Text jedes der zu versendenden Patches:

`git send-email -{{anzahl_an_commits}} --annotate`
