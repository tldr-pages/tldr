# nodemon

> Watch files and automatically restart a node application when changes are detected.
> More information: <https://github.com/remy/nodemon/tree/main/doc/cli>.

- Execute the specified file and watch a specific file for changes:

`nodemon {{path/to/file.js}}`

- Manually restart nodemon (note nodemon must already be active for this to work):

`rs`

- Ignore specific files:

`nodemon {{[-i|--ignore]}} {{path/to/file_or_directory}}`

- Pass arguments to the node application:

`nodemon {{path/to/file.js}} {{arguments}}`

- Pass arguments to node itself if they're not nodemon arguments already (e.g. `--inspect`):

`nodemon {{arguments}} {{path/to/file.js}}`

- Run an arbitrary non-node script:

`nodemon {{[-x|--exec]}} "{{command_to_run_script}} {{options}}" {{path/to/script}}`

- Run a Python script:

`nodemon {{[-x|--exec]}} "python {{options}}" {{path/to/file.py}}`
