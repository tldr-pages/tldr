# hg pull

> Pull changes from a specified repository to the local repository.

- Pull from the `default` source path:

`hg pull`

- Update the local repository to the head of the remote:

`hg pull {{path/to/source/repository}}`

- Update the local repository to the head of the remote:

`hg pull --update`

- Pull changes even when the remote repository is unrelated:

`hg pull --force`

- Specify a specific revision changeset to pull up to:

`hg pull --rev {{revision}}`

- Specify a specific branch to pull:

`hg pull --branch {{branch}}`

- Specify a specific bookmark to pull:

`hg pull --bookmark {{bookmark}}`
