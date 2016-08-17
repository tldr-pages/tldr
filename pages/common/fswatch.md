# fswatch

> A cross-platform file change monitor.

- Run a bash command on file creation, update or deletion:

`fswatch -0 {{path/to/watch}} | xargs -0 {{bash_command}}`

- Watch (multiple) directories or files

`fswatch -0 {{first/path/to/directory}} {{specificWatchedFile.js}} {{watchAllJsFiles/**/*.js}} | xargs -0 {{bash_command}}`

- Use `{}` in your bash command as a placeholder for the absolute path to the file change:

`fswatch -0 {{path/to/watch}} | xargs -0 -I {} {{bash_command}}`

- Filter by certain event type, eg. Updated, Deleted or Created:

`fswatch -0 --event {{Updated}} {{path/to/watch}} | xargs -0 {{bash_command}}`
