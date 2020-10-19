# inotifywait

> Waits for changes to one or more files.

- Run a command when a file changes:

`while inotifywait {{path/to/file}}; do {{command}}; done`

- Be quiet about watching for changes:

`while inotifywait --quiet {{path/to/file}}; do {{command}}; done`

- Watch a directory recursively for changes:

`while inotifywait --recursive {{path/to/directory}}; do {{command}}; done`

- Exclude files matching a regular expression:

`while inotifywait --recursive {{path/to/directory}} --exlude '{{regex}}'; do {{command}}; done`

- Wait at most 30 seconds:

`while inotifywait --timeout {{30}} {{path/to/file}}; do {{command}}; done`

- Only watch for file modification events:

`while inotifywait --event {{modify}} {{path/to/file}}; do {{command}}; done`
