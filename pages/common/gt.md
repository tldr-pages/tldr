# gt

> Create and manage sequences of dependent code changes (stacks) for Git and GitHub.
> More information: <https://graphite.dev/docs/get-started>.

- Initialise `gt` for the repository in the current directory:

`gt init`

- Create a new branch stacked on top of the current branch and commit staged changes:

`gt create {{branch_name}}`

- Create a new commit and fix upstack branches:

`gt modify -cam {{commit_message}}`

- Force push all branches in the current stack to GitHub and create or update PRs:

`gt stack submit`

- Checkout different branch (prompts interactive mode when branch name is omitted):

`gt co {{branch_name}}`

- Sync stack with remote version (also deletes merged branches):

`gt sync`

- Log all tracked stacks:

`gt log short`

- Display help for a specified subcommand:

`gt {{subcommand}} --help`
