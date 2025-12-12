# git grep

> Find strings inside tracked files in a repository.
> Accepts a lot of the same flags as regular `grep`.
> More information: <https://git-scm.com/docs/git-grep>.

- Search for a string in files in the current `HEAD`:

`git grep "{{search_string}}"`

- Search for a string in files matching a glob pattern in the current `HEAD`:

`git grep "{{search_string}}" -- "{{*.ext}}"`

- Search for a string, including submodules:

`git grep --recurse-submodules "{{search_string}}"`

- Search for a string at a specific point in history:

`git grep "{{search_string}}" {{HEAD~2}}`

- Search for a string across all branches and all of history:

`git grep "{{search_string}}" $(git rev-list --all)`
