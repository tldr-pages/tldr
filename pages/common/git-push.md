# git push

> Push commits to a remote repository.

- Publish local changes on a remote branch:

`git push {{remote_name}} {{local_branch}}`

- Publish local changes on a remote branch of different name:

`git push {{remote_name}} {{local_branch}}:{{remote_branch}}`

- Remove remote branch:

`git push {{remote_name}} :{{remote_branch}}`

- Remove remote branches which don't exist locally:

`git push --prune {{remote_name}}`

- Publish tags:

`git push --tags`
