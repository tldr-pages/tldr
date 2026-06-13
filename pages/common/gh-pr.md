# gh pr

> Manage GitHub pull requests.
> Some subcommands such as `create` have their own usage documentation.
> More information: <https://cli.github.com/manual/gh_pr>.

- Create a pull request:

`gh pr {{[new|create]}}`

- Check out a specific pull request locally:

`gh {{[co|pr checkout]}} {{pr_number|url|branch}}`

- View the changes made in the pull request for the current branch:

`gh pr diff`

- Approve the pull request for the current branch:

`gh pr review {{[-a|--approve]}}`

- Merge the pull request associated with the current branch interactively:

`gh pr merge`

- Edit a pull request interactively:

`gh pr edit`

- Edit the base branch of a pull request:

`gh pr edit {{[-B|--base]}} {{branch_name}}`

- Check the status of the current repository's pull requests:

`gh pr status`
