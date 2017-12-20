# hg push

> Push changes from the local repository to a specified destination.

- Push changes to the "default" remote path:

`hg push`

- Push changes to a specified remote repository:

`hg push {{path/to/destination_repository}}`

- Allow pushing a new branch (disabled by default):

`hg push --new-branch`

- Specify a specific revision changeset to push:

`hg push --rev {{revision}}`

- Specify a specific branch to push:

`hg push --branch {{branch}}`

- Specify a specific bookmark to push:

`hg push --bookmark {{bookmark}}`
