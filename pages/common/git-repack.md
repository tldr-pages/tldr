# git repack

> Pack unpacked objects in a Git repository.
> More information: <https://git-scm.com/docs/git-repack>.

- Pack unpacked objects in the current directory:

`git repack`

- Remove redundant objects after packing:

`git repack -d`

- Repack all objects into a single pack:

`git repack -a`

- Limit the repack to local objects only:

`git repack -l`
