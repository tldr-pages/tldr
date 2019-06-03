# browser-sync

> Starts local web server that updates browser on file changes.
> More information: <https://browsersync.io/docs/command-line>.

- Start a server from a specific directory:

`browser-sync start --server {{path/to/directory}} --files {{path/to/directory}}`

- Start a server from local directory, watching all css files in some directory:

`browser-sync start --server --files '{{path/to/directory/*.css}}'`

- Create configuration file:

`browser-sync init`

- Start browser-sync from config file:

`browser-sync start --config {{config_file}}`
