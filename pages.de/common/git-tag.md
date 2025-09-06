# git tag

> Erstelle, lösche, überprüfe und liste Tags auf.
> Weitere Informationen: <https://git-scm.com/docs/git-tag>.

- Liste alle Tags auf:

`git tag`

- Erstelle einen Tag mit Namen, welcher auf den aktuellen Commit zeigt:

`git tag {{tag_name}}`

- Erstelle einen Tag mit Namen, welcher auf einen bestimmten Commit zeigt:

`git tag {{tag_name}} {{commit}}`

- Erstelle einen Tag mit Anmerkung:

`git tag {{tag_name}} {{[-m|--message]}} {{anmkerung}}`

- Lösche einen Tag mit bestimmten Namen:

`git tag {{[-d|--delete]}} {{tag_name}}`

- Lade die aktualisierten Tags aus dem Upstream:

`git fetch {{[-t|--tags]}}`

- Liste alle Tags auf, bei denen sich in den vorangegangenen Commits ein bestimmter Commit findet:

`git tag --contains {{commit}}`
