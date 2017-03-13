# git

> Distributed version control system.

- Setup Git global configuration

`git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
git config --global core.editor vim`

- Initiate version control in the current directory, creating a .git folder

`git init`

- Review unstaged changes (paginate), deciding whether or not to add them to the commit

`git add -p`

- Show diff of staged changes

`git diff --cached`

- Commit changes with a short description

`git commit -m "Fixed something"`

- Delete last commit

`git reset --hard HEAD~1`

- Create and checkout a new branch

`git checkout -b mybranch`

- Check the Git version:

`git --version`

- Call general help:

`git --help`

- Call help on a command:

`git help {{command}}`

- Execute Git command:

`git {{command}}`
