# webpack

> Bundle your js files and other assets into a single output file.

- Create a single output file from an entry point file:

`webpack {{app.js}} {{bundle.js}}`

- Load css files too from your js file. (This uses the css loader for .css files):

`webpack {{app.js}} {{bundle.js}} --module-bind 'css=css'`

- Pass a config file and show compilation progress:

`webpack --config {{webpack.config.js}} --progress`

- Automatically recompile on file change:

`webpack --watch {{app.js}} {{bundle.js}}`
