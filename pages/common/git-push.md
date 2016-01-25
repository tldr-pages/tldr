# git push

> Push commits to a remote repository.

- Publish local changes on a remote branch:

`git push {{REMOTE-NAME}} {{LOCAL-BRANCH}}`

- Publish local changes on a remote branch of different name:

`git push {{REMOTE-NAME}} {{LOCAL-BRANCH}}:{{REMOTE-BRANCH}}`

- Remove remote branch:

`git push {{REMOTE-NAME}} :{{REMOTE-BRANCH}}`

- Remove remote branches which don't exist locally:

`git push --prune {{REMOTE-NAME}}`

- Publish tags:

`git push --tags`
