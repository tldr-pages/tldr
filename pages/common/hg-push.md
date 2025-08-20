# hg push

> Push changes from the local repository to a specified destination.
> More information: <https://www.mercurial-scm.org/help/commands/push>.

- Push changes to the "default" remote path:

`hg push`

- Push changes to a specified remote repository:

`hg push {{path/to/destination_repository}}`

- Push a new branch if it does not exist (disabled by default):

`hg push --new-branch`

- Specify a specific revision changeset to push:

`hg push {{[-r|--rev]}} {{revision}}`

- Specify a specific branch to push:

`hg push {{[-b|--branch]}} {{branch}}`

- Specify a specific bookmark to push:

`hg push {{[-B|--bookmark]}} {{bookmark}}`
