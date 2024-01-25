# inotifywait

> Waits for changes to files.
> More information: <https://manned.org/inotifywait>.

- Watch a specific file for events, exiting after the first one:

`inotifywait {{path/to/file}}`

- Continuously watch a specific file for events without exiting:

`inotifywait --monitor {{path/to/file}}`

- Watch a directory recursively for events:

`inotifywait --monitor --recursive {{path/to/directory}}`

- Watch a directory for changes, excluding files, whose names match a regular expression:

`inotifywait --monitor --recursive --exclude "{{regular_expression}}" {{path/to/directory}}`

- Watch a file for changes, exiting when no event occurs for 30 seconds:

`inotifywait --monitor --timeout {{30}} {{path/to/file}}`

- Only watch a file for file modification events:

`inotifywait --event {{modify}} {{path/to/file}}`

- Watch a file printing only events, and no status messages:

`inotifywait --quiet {{path/to/file}}`

- Run a command when a file is accessed:

`inotifywait --event {{access}} {{path/to/file}} && {{command}}`
