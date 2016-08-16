# fswatch

> A cross-platform file change monitor.

- Run a single bash command on file change:

`fswatch -0 {{paths_to_watch}} | xargs -0 -n 1 -I {} {{bash_command}}`
