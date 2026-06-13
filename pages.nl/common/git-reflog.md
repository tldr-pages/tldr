# git reflog

> Toon een log met veranderingen in lokale referenties zoals HEAD, branches en tags.
> Meer informatie: <https://git-scm.com/docs/git-reflog>.

- Toon de reflog voor HEAD:

`git reflog`

- Toon de reflog voor een bepaalde branch:

`git reflog {{branch_naam}}`

- Toon alleen de laatste 5 vermeldingen in de reflog:

`git reflog {{[-n|--max-count]}} 5`
