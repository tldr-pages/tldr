# hg pull

> Pull changes from a specified repository to the local repository.
> More information: <https://www.mercurial-scm.org/doc/hg.1.html#pull>.

- Pull from the "default" source path:

`hg pull`

- Pull from a specified source repository:

`hg pull {{path/to/source_repository}}`

- Update the local repository to the head of the remote:

`hg pull {{[-u|--update]}}`

- Pull changes even when the remote repository is unrelated:

`hg pull {{[-f|--force]}}`

- Specify a specific revision changeset to pull up to:

`hg pull {{[-r|--rev]}} {{revision}}`

- Specify a specific branch to pull:

`hg pull {{[-b|--branch]}} {{branch}}`

- Specify a specific bookmark to pull:

`hg pull {{[-B|--bookmark]}} {{bookmark}}`
