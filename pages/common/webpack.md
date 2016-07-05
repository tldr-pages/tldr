# webpack

> Bundle a web project's js files and other assets into a single output file.

- Create a single output file from an entry point file:

`webpack {{app.js}} {{bundle.js}}`

- Load css files too from your js file. (This uses the css loader for .css files):

`webpack {{app.js}} {{bundle.js}} --module-bind 'css=css'`

- Pass a config file and show compilation progress. (As an example config, you can export an object containing `entry` and `output.filename` properties, which correspond to the entry and output file names):

`webpack --config {{webpack.config.js}} --progress`

- Automatically recompile on changes to project files:

`webpack --watch {{app.js}} {{bundle.js}}`
