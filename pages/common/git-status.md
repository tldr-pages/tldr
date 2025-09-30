# git status

> Show the changes to files in a Git repository.
> List changed, added and deleted files compared to the currently checked-out commit.
> More information: <https://git-scm.com/docs/git-status>.

- Show changed files which are not yet added for commit:

`git status`

- Give output in short format:

`git status {{[-s|--short]}}`

- Show verbose information on changes in both the staging area and working directory:

`git status {{[-vv|--verbose --verbose]}}`

- Show the branch and tracking info:

`git status {{[-b|--branch]}}`

- Show output in short format along with branch info:

`git status {{[-sb|--short --branch]}}`

- Show the number of entries currently stashed away:

`git status --show-stash`

- Don't show untracked files in the output:

`git status {{[-uno|--untracked-files=no]}}`
