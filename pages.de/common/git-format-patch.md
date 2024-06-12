# git format-patch

> Erstelle .patch Dateien. Ermöglicht Commits per Email zu senden.
> Siehe auch `git am`, womit .patch Datein lokal angewandt werden.
> Weitere Informationen: <https://git-scm.com/docs/git-format-patch>.

- Erzeuge eine `.patch` Datei aus allen nicht gepushten Commits:

`git format-patch {{origin}}`

- Erstelle eine `.patch` Datei aus allen Commits zwischen den Revision und schreibe diese nach `stdout`:

`git format-patch {{revision_1}}..{{revision_2}}`

- Erstelle ein `.patch` Datei aus den letzten 3 Commits:

`git format-patch -{{3}}`
