# gh repo

> Work with GitHub repositories on the command line.
> More information: <https://cli.github.com/manual/gh_repo>.

- Create a new repository (if the repository name is not set, the default name will be the name of the current directory):

`gh repo create {{name}}`

- Clone a repository:

`gh repo clone {{owner}}/{{repository}}`

- Fork and clone a repository:

`gh repo fork {{owner}}/{{repository}} --clone`

- View a repository in the web browser:

`gh repo view {{repository}} --web`
