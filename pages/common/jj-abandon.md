# jj abandon

> Abandon a revision, rebasing descendants onto its parent(s).
> Abandoning a revision removes its associated change ID.
> More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-abandon>.

- Abandon revisions specified by given revsets (e.g. `B::D`, `A..D`, `B|C|D`, etc.):

`jj abandon {{revsets}}`

- Abandon revisions, without deleting their bookmarks and moving them to the parent revisions instead:

`jj abandon --retain-bookmarks {{revsets}}`

- Abandon revisions, without modifying the contents of their children:

`jj abandon --restore-descendants {{revsets}}`
