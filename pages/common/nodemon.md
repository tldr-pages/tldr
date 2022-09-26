# nodemon

> Watch files and automatically restart a node application when changes are detected.
> More information: <https://nodemon.io>.

- Execute the specified file and watch a specific file for changes:

`nodemon {{path/to/file.js}}`

- Manually restart nodemon (note nodemon must already be active for this to work):

`rs`

- Ignore specific files:

`nodemon --ignore {{path/to/file_or_directory}}`

- Pass arguments to the node application:

`nodemon {{path/to/file.js}} {{arguments}}`

- Pass arguments to node itself if they're not nodemon arguments already (e.g. `--inspect`):

`nodemon {{arguments}} {{path/to/file.js}}`

- Run an arbitrary non-node script:

`nodemon --exec "{{command_to_run_script}} {{options}}" {{path/to/script}}`

- Run a Python script:

`nodemon --exec "python {{options}}" {{path/to/file.py}}`
