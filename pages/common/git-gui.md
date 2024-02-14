# git gui

> A GUI for making new commits, amending existing ones, creating branches, performing local merges, and fetching/pushing to remote repositories.
> See also: `git-cola`, `gitk`.
> More information: <https://git-scm.com/docs/git-gui>.

- Launch the GUI:

`git gui`

- Show a specific file with author name and commit hash on each line:

`git gui blame {{path/to/file}}`

- Open `git gui blame` in a specific revision:

`git gui blame {{revision}} {{path/to/file}}`

- Open `git gui blame` by scrolling the view to center on a specific line:

`git gui blame --line={{line}} {{path/to/file}}`

- Open a window to make one commit and return to the shell when it is complete:

`git gui citool`

- Open `git gui citool` in the "Amend Last Commit" mode:

`git gui citool --amend`

- Open `git gui citool` in a read-only mode:

`git gui citool --nocommit`

- Show a browser for the tree of a specific branch, opening the blame tool when clicking on the files:

`git gui browser maint`
