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

- Show what revision and author last modified each line of a file

`git blame {{file}}`

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

- Reset current HEAD to the previous commit and preserve all unstaged changes

`git reset {{commit}}`

- Discard all local uncommitted changes

`git reset --hard HEAD`

- Checking git version

`git --version`

- Calling help

`git --help`

- Executing git command

`git {{command}}`