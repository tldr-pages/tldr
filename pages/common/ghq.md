# ghq

> Manage remote repository clones organized by hostname and path.
> More information: <https://github.com/x-motemen/ghq>.

- Clone a repository under the `ghq` root directory (default is `~/ghq`):

`ghq get {{repository_url}}`

- Clone a repository from a user/project format (defaults to GitHub):

`ghq get {{user}}/{{project}}`

- Clone a repository and `cd` into it:

`ghq get {{repository_url}} --look`

- Clone a repository via SSH:

`ghq get {{user}}/{{project}} -p`

- Update an existing repository to the latest version:

`ghq get {{repository_url}} -u`

- List all locally cloned repositories:

`ghq list`

- List locally cloned repositories with full paths:

`ghq list --full-path`

- Remove a locally cloned repository:

`ghq rm {{user}}/{{project}}`
