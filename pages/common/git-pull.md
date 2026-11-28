# git pull

> Fetch branch from a remote repository and merge it to local repository.
> More information: <https://git-scm.com/docs/git-pull>.

- Download changes from default remote repository and merge it:

`git pull`

- Download changes from default remote repository and rebase local commits on top of them:

`git pull {{[-r|--rebase]}}`

- Download changes from a specific remote repository:

`git pull {{remote_name}}`

- Download changes from given remote repository and branch, then merge them into `HEAD`:

`git pull {{remote_name}} {{branch}}`
