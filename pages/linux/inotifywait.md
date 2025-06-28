# inotifywait

> Waits for changes to files.
> More information: <https://manned.org/inotifywait>.

- Watch a specific file for events, exiting after the first one:

`inotifywait {{path/to/file}}`

- Continuously watch a specific file for events without exiting:

`inotifywait {{[-m|--monitor]}} {{path/to/file}}`

- Watch a directory recursively for events:

`inotifywait {{[-m|--monitor]}} {{[-r|--recursive]}} {{path/to/directory}}`

- Watch a directory for changes, excluding files, whose names match a regular expression:

`inotifywait {{[-m|--monitor]}} {{[-r|--recursive]}} --exclude "{{regular_expression}}" {{path/to/directory}}`

- Watch a file for changes, exiting when no event occurs for 30 seconds:

`inotifywait {{[-m|--monitor]}} {{[-t|--timeout]}} {{30}} {{path/to/file}}`

- Only watch a file for file modification events:

`inotifywait {{[-e|--event]}} {{modify}} {{path/to/file}}`

- Watch a file printing only events, and no status messages:

`inotifywait {{[-q|--quiet]}} {{path/to/file}}`

- Run a command when a file is accessed:

`inotifywait {{[-e|--event]}} {{access}} {{path/to/file}} && {{command}}`
