# dvc diff

> Show changes in DVC tracked file and directories.
> More information: <https://dvc.org/doc/command-reference/diff>.

- Compare DVC tracked files from different Git commits, tags, and branches w.r.t the current workspace:

`dvc diff {{commit_hash/tag/branch}}`

- Compare DVC tracked file in Git b_rev w.r.t a_rev:

`dvc diff b_rev a_rev`

- Compare DVC tracked files, along with their latest hash:

`dvc diff --show-hash {{commit}}`

- Compare DVC tracked files, displaying the output as JSON:

`dvc diff --show-json --show-hash {{commit}}`

- Compare DVC tracked files, displaying the output as Markdown:

`dvc diff --show-md --show-hash {{commit}}`
