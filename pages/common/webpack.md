# webpack

> Bundle a web project's js files and other assets into a single output file.
> More information: <https://webpack.js.org>.

- Create a single output file from an entry point file:

`webpack {{app.js}} {{bundle.js}}`

- Load css files too from the js file (this uses the css loader for `.css` files):

`webpack {{app.js}} {{bundle.js}} --module-bind 'css=css'`

- Pass a config file (with eg. the entry script and the output filename) and show compilation progress:

`webpack --config {{webpack.config.js}} --progress`

- Automatically recompile on changes to project files:

`webpack --watch {{app.js}} {{bundle.js}}`
