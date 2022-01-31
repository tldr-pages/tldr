# gh pr merge

> Merge GitHub pull requests.
> More information: <https://cli.github.com/manual/gh_pr_merge>.

- Merge the pull request associated with the current branch interactively:

`gh pr merge`

- Merge the specified pull request, interactively:

`gh pr merge {{pr_number}}`

- Merge the pull request, removing the branch on both the local and the remote:

`gh pr merge --delete-branch`

- Merge the current pull request with the specified merge strategy:

`gh pr merge --{{merge|squash|rebase}}`

- Merge the current pull request with the specified merge strategy and commit message:

`gh pr merge --{{merge|squash|rebase}} --subject {{commit_message}}`

- Squash the current pull request into one commit with the message body and merge:

`gh pr merge --squash --body="{{commit_message_body}}"`

- Display help:

`gh pr merge --help`
