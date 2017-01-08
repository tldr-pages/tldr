# git push

> Push commits to a remote (upstream) repository.

- Send local changes in the current branch to its remote counterpart:

`git push`

- Send local changes in a given branch to its remote counterpart:

`git push {{remote_name}} {{local_branch}}`

- Publish the current branch to a remote repository, setting the upstream branch name:

`git push {{remote_name}} -u {{remote_branch}}`

- Send changes on all local branches to their remote counterparts:

`git push --all`

- Delete a branch in a remote repository:

`git push {{remote_name}} --delete {{remote_branch}}`

- Remove local references to branches that have been deleted in a remote repository:

`git push --prune {{remote_name}}`

- Publish tags that aren't yet in the remote repository:

`git push --tags`
