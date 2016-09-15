# fswatch

> A cross-platform file change monitor.

- Run a bash command on file creation, update or deletion:

`fswatch -0 {{path/to/file}} | xargs -0 {{bash_command}}`

- Watch one or more files and/or directories:

`fswatch -0 {{path/to/file}} {{path/to/directory}} {{path/to/another_directory/**/*.js}} | xargs -0 {{bash_command}}`

- Use `{}` in your bash command as a placeholder for the absolute path to the changed file:

`fswatch -0 {{path/to/directory}} | xargs -0 -I {} {{bash_command}}`

- Filter by event type, eg. Updated, Deleted or Created:

`fswatch -0 --event {{Updated}} {{path/to/directory}} | xargs -0 {{bash_command}}`
