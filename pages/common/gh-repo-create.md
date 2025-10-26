# gh repo create

> Create a new GitHub repository.
> Note: `--public`, `--private`, or `--internal` required when not running interactively.
> More information: <https://cli.github.com/manual/gh_repo_create>.

- Create a new repository interactively:

`gh repo {{[new|create]}}`

- Create a private repository from the current directory:

`gh repo {{[new|create]}} {{[-s|--source]}} . --private`

- Create a public repository from the current directory:

`gh repo {{[new|create]}} {{[-s|--source]}} . --public`

- Create a public repository with a specified name and description:

`gh repo {{[new|create]}} {{repo_name}} {{[-d|--description]}} "{{repo_description}}" --public`

- Clone the new repository locally after creation:

`gh repo {{[new|create]}} {{repo_name}} {{[-c|--clone]}} {{--public|--private|--internal}}`
