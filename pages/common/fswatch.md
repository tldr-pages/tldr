# fswatch

> A cross-platform file change monitor.
> More information: <https://emcrisostomo.github.io/fswatch>.

- Run a Bash command on file creation, update or deletion:

`fswatch {{path/to/file}} | xargs -n 1 {{bash_command}}`

- Watch one or more files and/or directories:

`fswatch {{path/to/file}} {{path/to/directory}} {{path/to/another_directory/**/*.js}} | xargs -n 1 {{bash_command}}`

- Print the absolute paths of the changed files:

`fswatch {{path/to/directory}} | xargs -n 1 -I {} echo {}`

- Filter by event type:

`fswatch --event {{Updated|Deleted|Created}} {{path/to/directory}} | xargs -n 1 {{bash_command}}`
