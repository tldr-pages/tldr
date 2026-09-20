# jj run

> Run a command across a set of revisions, amending each with the resulting changes.
> Each revision is checked out into an isolated working copy before the command runs.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-run>.

- Run a command on the current revision:

`jj run -- {{command}}`

- Run a command across a revset:

`jj run {{[-r|--revision]}} {{revset}} -- {{command}}`

- Run a formatter across all commits in a stack:

`jj run {{[-r|--revision]}} 'trunk()..@' -- cargo fmt`

- Print the change ID of each revision in a revset (`$JJ_CHANGE_ID` is set by `jj run` for each revision):

`jj run {{[-r|--revision]}} {{revset}} -- sh -c 'echo $JJ_CHANGE_ID'`

- Run a command in parallel across multiple revisions:

`jj run {{[-r|--revision]}} {{revset}} {{[-j|--jobs]}} {{num_jobs}} -- {{command}}`

- Run a command without rewriting any commits (dry-run):

`jj run --ignore-changes {{[-r|--revision]}} {{revset}} -- {{command}}`

- Run a command while keeping descendants' content unchanged:

`jj run --restore-descendants {{[-r|--revision]}} {{revset}} -- {{command}}`

- Run a command from the workspace root instead of each revision's root:

`jj run {{[-r|--revision]}} {{revset}} --root -- {{command}}`
