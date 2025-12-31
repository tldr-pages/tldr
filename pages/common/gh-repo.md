# gh repo

> Work with GitHub repositories.
> More information: <https://cli.github.com/manual/gh_repo>.

- Create a new repository interactively:

`gh repo {{[new|create]}}`

- Clone a repository:

`gh repo clone {{owner}}/{{repository}}`

- Fork and clone a repository:

`gh repo fork {{owner}}/{{repository}} --clone`

- View a repository in the default web browser:

`gh repo view {{repository}} {{[-w|--web]}}`

- List repositories owned by a specific user or organization (if the owner is not set, the default owner will be the currently logged in user):

`gh repo {{[ls|list]}} {{owner}}`

- List only non-forks repositories and limit the number of repositories to list (default: 30):

`gh repo {{[ls|list]}} {{owner}} --source {{[-L|--limit]}} {{limit}}`

- List repositories with a specific primary coding language:

`gh repo {{[ls|list]}} {{owner}} {{[-l|--language]}} {{language_name}}`
