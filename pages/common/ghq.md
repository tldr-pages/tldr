# ghq

> Manage remote repository clones organized by hostname and path.
> More information: <https://github.com/x-motemen/ghq>.

- Clone a repository under the ghq root directory (default is `~/ghq`):

`ghq get {{repository_url}}`

- Clone a repository from a user/project format (defaults to GitHub):

`ghq get {{user}}/{{project}}`

- Clone a repository and cd into it:

`ghq get -look {{repository_url}}`

- Clone a repository via SSH using the `-p` flag:

`ghq get -p {{user}}/{{project}}`

- Clone a repository with a shallow clone (Git only):

`ghq get --shallow {{repository_url}}`

- Update an existing repository to the latest version:

`ghq get -u {{repository_url}}`

- List all locally cloned repositories:

`ghq list`

- List all locally cloned repositories with full paths:

`ghq list --full-path`

- List locally cloned repositories matching a query:

`ghq list {{query}}`

- Remove a locally cloned repository:

`ghq rm {{user}}/{{project}}`

- Display the path to the ghq root directory:

`ghq root`

- Create a new repository in the ghq root:

`ghq create {{user}}/{{project}}`
