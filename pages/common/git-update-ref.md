# git update-ref

> Git command for creating, updating, and deleting Git refs.
> More information: <https://git-scm.com/docs/git-update-ref>.

- Delete a ref, useful for soft resetting the first commit:

`git update-ref -d {{HEAD}}`

- Update ref with a message:

`git update-ref -m {{message}} {{HEAD}} {{4e95e05}}`
