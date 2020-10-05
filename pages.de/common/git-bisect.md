# git bisect

> Benuzt binäre Suche um den commit ausfindig zu machen, welcher einen Fehler beinhaltet.
> Git springt im Commit-Graph automatisch vor und zurück, um denfehlerhaften Commit schrittweise einzugrenzen zu können.
> Mehr Informationen: <https://git-scm.com/docs/git-bisect>.

- Startet eine Bisect-Session in einem Commit-Bereich, der durch einen bekannten fehlerhaften Commit und einen sauber Commit begrenzt wird:

`git bisect start {{bad_commit}} {{good_commit}}`

- Jeder Commit, den `git bisect` auswählt, wird geprüft und mit "gut" oder "schlecht" gekennzeichnet:

`git bisect {{good|bad}}`

- Nachdem "git bisect" den fehlerhaften Commit lokalisiert hat kann mit 'git bisect reset' zum vorherigen Branch zurück gewechselt werden:

`git bisect reset`

- Überspringen einen Commit während der Bisect-Session (z.B. einen, der die Tests aufgrund eines anderen Problems nicht bestanden hat):

`git bisect skip`
