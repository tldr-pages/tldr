# git tag

> Erstelle, lösche, liste sie auf und überprüfe Tags.
> Ein Tag ist eine statische Referenz auf einen bestimmten Commit.
> Mehr Informationen: <https://git-scm.com/docs/git-tag>.

- Liste alle Tags auf:

`git tag`

- Erstelle einen Tag mit Namen, welcher auf den aktuellen Commit zeigt:

`git tag {{name_des_tags}}`

- Erstelle einen Tag mit Namen, welcher auf einen bestimmten Commit zeigt:

`git tag {{name_des_tags}} {{commit}}`

- Erstelle einen Tag mit Anmerkung:

`git tag {{name_des_tags}} -m {{anmkerung}}`

- Lösche einen Tag mit bestimmten Namen:

`git tag -d {{name_des_tags}}`

- Lade die aktualisierten Tags aus dem Upstream:

`git fetch --tags`

- Liste alle Tags auf, bei denen sich in den vorangegangenen Commits ein bestimmter Commit findet:

`git tag --contains {{commit}}`
