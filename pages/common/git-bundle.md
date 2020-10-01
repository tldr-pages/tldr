# git bundle

> Package objects and references into an archive.
> More information: <https://git-scm.com/docs/git-bundle>.

- Create a bundle file that contains all objects and references of a specific branch:

`git bundle create {{path/to/file.bundle}} {{branch_name}}`

- Create a bundle file of all branches:

`git bundle create {{path/to/file.bundle}} --all`

- Create a bundle file of the last 5 commits of the current branch:

`git bundle create {{path/to/file.bundle}} -{{5}} {{HEAD}}`

- Create a bundle file of the latest 7 days:

`git bundle create {{path/to/file.bundle}} --since={{7.days}} {{HEAD}}`

- Verify that a bundle file is valid and can be applied to the current repository:

`git bundle verify {{path/to/file.bundle}}`

- Print to the standard output the list of references contained in a bundle:

`git bundle unbundle {{path/to/file.bundle}}`

- Unbundle a specific branch from a bundle file into the current repository:

`git pull {{path/to/file.bundle}} {{branch_name}}`
