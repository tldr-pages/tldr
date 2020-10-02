# legit

> Legit is a complementary command-line interface for Git
> More information: <https://frostming.github.io/legit>.

- Switches to branch. Stashes and restores unstaged changes.
`git switch <branch>`

- Synchronizes current branch. Auto-merge/rebase, un/stash.
`git sync`

- Publishes branch to remote server.
`git publish {{branch}}`

- Removes branch from remote server.
`git unpublish {{branch}}`

- Nice & pretty list of branches + publication status.
`git branches {{wildcard pattern}}`

- Removes the last commit from history.
`git undo {{--hard}}`
