# dvc diff

> Show changes in DVC tracked file and directories added/deleted/modified
> More information: <https://dvc.org/doc/command-reference/diff>.

- Compare DVC tracked file from different Git commit/tag/branch w.r.t current workspace:

`dvc diff {{commit_hash/tag/branch}}`

- Compare DVC tracked file in Git b_rev w.r.t a_rev:

`dvc diff b_rev a_rev`

- Compare DVC tracked file, along with their latest hash:

`dvc diff --show-hash {{commit}}`

- Compare DVC tracked file, get output in JSON format:

`dvc diff --show-json --show-hash {{commit}}`

- Compare DVC tracked file, get output in Markdown format:

`dvc diff --show-md --show-hash {{commit}}`
