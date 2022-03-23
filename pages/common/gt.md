# gt

> Create and manage sequences of dependent code changes (stacks) for `git` and GitHub.
> More information: <https://docs.graphite.dev/>.

- Authenticate the CLI with GitHub:

`gt auth --token {{your_cli_auth_token}}`

- Initialise `gt` for the current repo:

`gt repo init`

- Create a new branch stacked on top of the current branch and commit staged changes with:

`gt bc {{branch_name}}`

- Create a new commit and fix upstack branches:

`gt cc -m {{commit_message}}`

- Force push all branches in the current stack to GitHub and create or update a PRs:

`gt ss`

- Log all tacked stacks:

`gt ls`

- List help documentation:

`gt {{subcommand}} --help`
