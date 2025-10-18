# git-filter-branch

> Change branch history, like removing files.
> More information: <https://git-scm.com/docs/git-filter-branch>.

- Remove a file from all commits:

`git filter-branch --tree-filter 'rm -f {{file}}' HEAD`

- Update author email:

`git filter-branch --env-filter 'GIT_AUTHOR_EMAIL={{new_email}}' HEAD`

- Delete a folder from history:

`git filter-branch --tree-filter 'rm {{[-rf|--recursive --force]}} {{folder}}' HEAD`
