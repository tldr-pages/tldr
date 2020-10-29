# gh repo

> Work with GitHub repositories on the command line.
> More information: <https://cli.github.com/manual/gh_repo>.

- Create new repository (if the repository name is not set, it will default to the name of the current directory):

`gh repo create {{name}}`

- Clone repository:

`gh repo clone {{repository}}`

- Fork and clone repository:

`gh repo fork {{owner}}/{{repository}} --clone=true`

- View a repository in the web browser:

`gh repo view {{repository}} --web`
