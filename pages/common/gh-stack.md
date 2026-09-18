# gh stack

> A GitHub CLI extension for managing stacked branches and pull requests.
> More information: <https://docs.github.com/en/pull-requests/reference/stacked-prs-cli-commands>.

- Start a new stack interactively (creates and checks out the first branch):

`gh stack init`

- Start a new stack specifying branches upfront:

`gh stack init {{branch_name1}} {{branch_name2}}`

- Add a branch on top of the stack:

`gh stack add {{branch_name}}`

- Push all branches:

`gh stack push`

- View the stack:

`gh stack view`

- Open a stack of PRs:

`gh stack submit`
