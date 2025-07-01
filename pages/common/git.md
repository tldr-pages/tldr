# git

> Distributed version control system.
> Some subcommands such as `commit`, `add`, `branch`, `switch`, `push`, etc. have their own usage documentation.
> More information: <https://git-scm.com/docs/git>.

- Create an empty git repository:

`git init`

- Clone a git repository from the internet:

`git clone {{https://example.com/repo.git}}`

- View the status of the current repository:

`git status`

- Stage all chages for a commit:

`git add {{[-A|-all]}}`

- Commit changes to version history

`git commit {{[-m|--message]}} {{message-text}}`

- Push version history to a remote

`git push`

- Pull any changes made to a remote

`git pull`

- Reset everything the way it was in the latest commit:

`git reset --hard; git clean {{[-f|--force]}}`
