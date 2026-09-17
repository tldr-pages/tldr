# jj util

> Infrequently used utility commands for Jujutsu.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-util>.

- Generate shell completion script:

`jj util completion {{bash|fish|nushell|zsh}}`

- Execute an external command in the workspace:

`jj util exec -- {{command}}`

- Run garbage collection on obsolete objects and abandoned operations older than 2 weeks:

`jj util gc`

- Run garbage collection immediately without waiting for the default expiration:

`jj util gc --expire now`

- Explicitly snapshot the working copy:

`jj util snapshot`

- Print the JSON schema for the Jujutsu configuration format:

`jj util config-schema`

- Print the name of the backend used in the current repository:

`jj util backend name`

- Install Jujutsu's man pages to a directory:

`jj util install-man-pages {{path/to/directory}}`
