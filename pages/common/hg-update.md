# hg update

> Update the working directory to a specified changeset.
> More information: <https://www.mercurial-scm.org/doc/hg.1.html#update>.

- Update to the tip of the current branch:

`hg update`

- Update to the specified revision:

`hg update --rev {{revision}}`

- Update and discard uncommitted changes:

`hg update --clean`

- Update to the last commit matching a specified date:

`hg update --date {{dd-mm-yyyy}}`
