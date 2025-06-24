# gh repo create

> Create a new GitHub repository using the GitHub CLI.
> More information: <https://cli.github.com/manual/gh_repo_create>.

- Create a new repository interactively:

`gh repo create`

- Create a new repository with a specified name and description:

`gh repo create {{repo_name}} --description "{{repo_description}}"`

- Create a private repository from the current directory:

`gh repo create --private`

- Clone the new repo locally after creation:

`gh repo create {{repo_name}} --clone`

- Push the current directory to a new GitHub repository:

`gh repo create --source . --public`
