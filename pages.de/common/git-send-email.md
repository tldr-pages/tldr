# git send-email

> Sende Patches als Email. Möglich für einzelene Commits, Ordner oder .patch Datein.
> Weitere Informationen: <https://git-scm.com/docs/git-send-email>.

- Sende den letzten Commit der aktuellen Branch:

`git send-email -1`

- Sende einen spezifischen Commmit:

`git send-email -1 {{commit}}`

- Sende die letzten (z.B. 10) Commits der aktuellen Branch:

`git send-email {{-10}}`

- Sende eine Einleitungs Email für eine Reihe von Patches:

`git send-email -{{Anzahl_an_Committs}} --compose`

- Bearbeiten des Email Textes von jedem der Patches:

`git send-email -{{Anzahl_an_Committs}} --annotate`
