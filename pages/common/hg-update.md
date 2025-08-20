# hg update

> Update the working directory to a specified changeset.
> More information: <https://www.mercurial-scm.org/help/commands/update>.

- Update to the tip of the current branch:

`hg update`

- Update to the specified revision:

`hg update {{[-r|--rev]}} {{revision}}`

- Update and discard uncommitted changes:

`hg update {{[-C|--clean]}}`

- Update to the last commit matching a specified date:

`hg update {{[-d|--date]}} {{dd-mm-yyyy}}`
