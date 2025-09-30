# gh repo create

> Create a new GitHub repository.
> More information: <https://cli.github.com/manual/gh_repo_create>.

- Create a new repository interactively:

`gh repo {{[new|create]}}`

- Create a new repository with a specified name and description:

`gh repo {{[new|create]}} {{repo_name}} {{[-d|--description]}} "{{repo_description}}"`

- Create a private repository from the current directory:

`gh repo {{[new|create]}} {{[-s|--source]}} . --private`

- Clone the new repository locally after creation:

`gh repo {{[new|create]}} {{repo_name}} {{[-c|--clone]}}`

- Push the current directory to a new GitHub repository:

`gh repo {{[new|create]}} {{[-s|--source]}} . --public`
