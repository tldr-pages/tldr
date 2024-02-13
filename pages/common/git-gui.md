# git gui

> A GUI for making new commits, amending existing ones, creating branches, performing local merges, and fetching/pushing to remote repositories.
> See also: `git-cola`, `gitk`.
> More information: <https://git-scm.com/docs/git-gui>.

- Launch the GUI:

`git gui`

- Show a specific file with author name and commit hash on each line:

`git gui blame {{path/to/file}}`

- Show a specific file with author name and commit hash on each line in a specific revision:

`git gui blame {{revision}} Makefile`

- Show a specific file with author name and commit hash on each line scrolling the view to center on a specific line:

`git gui blame --line={{line}} Makefile`

- Make one commit and return to the shell when it is complete:

`git gui citool`

- Make one commit entering the Amend Last Commit mode of the interface:

`git gui citool --amend`

- Check if the index does not contain any unmerged entries:

`git gui citool --nocommit`

- Show a browser for the tree of a specific branch, opening the blame tool when clicking on the files:

`git gui browser maint`
