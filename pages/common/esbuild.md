# esbuild

> An extremely fast JavaScript bundler and minifier.
> More information: <https://esbuild.github.io/>.

- Bundle a JavaScript code and print to stdout:

`esbuild --bundle {{path/to/file.js}}`

- Bundle a JSX application from stdin:

`esbuild --bundle --outfile={{path/to/out.js}} < {{path/to/file.jsx}}`

- Bundle and minify a JSX application with source maps in `production` mode:

`esbuild --bundle --define:{{process.env.NODE_ENV=\"production\"}} --minify --sourcemap {{path/to/file.js}}`

- Bundle a JSX application for a comma-separated list of browsers:

`esbuild --bundle --minify --sourcemap --target={{browser(s)}} {{path/to/file.jsx}}`

- Bundle a JavaScript code for a specific node version:

`esbuild --bundle --platform={{node}} --target={{node12}} {{path/to/file.js}}`

- Bundle a JavaScript code enabling JSX syntax in `.js` files:

`esbuild --bundle app.js --loader:.js=jsx {{path/to/file.js}}`

- Bundle and serve a JavaScript file:

`esbuild --bundle --serve={{port}} --outfile={{index.js}} {{path/to/file.js}}`

- Bundle a space-separated list of files to an output directory:

`esbuild --bundle --outdir={{path/to/output_directory}} {{path/to/files(s)}}`
