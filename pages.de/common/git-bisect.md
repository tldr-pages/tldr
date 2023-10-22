# git bisect

> Benutzt binäre Suche um den commit ausfindig zu machen, welcher einen Fehler beinhaltet.
> Git springt im Commit-Graph automatisch vor und zurück, um den fehlerhaften Commit schrittweise eingrenzen zu können.
> Weitere Informationen: <https://git-scm.com/docs/git-bisect>.

- Starte eine Bisect-Session in einem Commit-Bereich, der durch einen bekannten fehlerhaften Commit und einen sauberen Commit begrenzt wird:

`git bisect start {{fehlerhafter_commit}} {{sauberer_commit}}`

- Prüfe jeden Commit, den `git bisect` auswählt, und kennzeichne ihn mit "gut" oder "schlecht":

`git bisect {{good|bad}}`

- Wechsle zum vorherigen Branch zurück, nachdem der fehlerhafte Commit lokalisiert wurde:

`git bisect reset`

- Überspringe einen Commit während der Bisect-Session (z.B. einen, der die Tests aufgrund eines anderen Problems nicht bestanden hat):

`git bisect skip`
