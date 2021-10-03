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

- Run non-node scripts:

`nodemon --exec "{{python --verbose}}" {{path/to/file.py}}`
