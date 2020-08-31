# nodemon

> Automatically restart node application when watched files are changed.
> More information: <https://nodemon.io>.

- Watch a spesific file for reloads:

`nodemon --inspect filename.js`

- Manually restart nodemon (note nodemon must already be active for this to work):

`rs`

- Ignore specific files:

`nodemon --ignore {{path/to/file_or_directory}}`

- Pass arguments to your node application:

`nodemon {{path/to/file.js}} {{arguments}}`

- Running non-node scripts:

`nodemon --exec "{{command}}" {{path/to/script_file}}`
