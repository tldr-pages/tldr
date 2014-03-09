#git

> Main command for all `git` commands

- Create a new local repository

`git init`

- Show changed files which are not yet added for commit

`git status`

- Show changes to tracked files

`git diff`

- Add all current changes to the next commit

`git add .`

- Commit staged files to the repository with comment

`git commit -am "Commit message"`

- Replace the last commit with currently staged changes

`git commit --amend`

- Show all commits

`git log`

- Clone an existing repository

`git clone {{remote-repository-location}}`

- List all existing branches

`git branch`

- Create new branch based on current branch

`git branch {{new-branch}}`

- Switch to another branch

`git checkout {{another-branch}}`

- Delete a local branch

`git branch -d {{branch-name}}`

- Download repository from remote location and merge with current local branch

`git pull {{remote-repository}} {{local-branch}}`

- Publish local changes on a remote location

`git push {{remote-repository}} {{local-branch}}`

- Merge a branch with your current HEAD branch

`git merge {{branch-name}}`

- stash current local changes in a temporary area

`git stash {{optional_stash_name}}`

- include new files in the stash (leaves the index completely clean)

`git stash -u {{optional_stash_name}}`

- list all stashes

`git stash list`

- re-apply the latest stash

`git stash pop`

- re-apply a stash by name

`git stash apply {{stash_name}}`

- Calling help

`git --help`
