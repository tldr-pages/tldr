# ncc

> Compile a Node.js project into a single file.
> Supports TypeScript, binary addons and dynamic requires.
> More information: <https://github.com/vercel/ncc>.

- Bundle a JavaScript application:

`ncc build {{path/to/file.js}}`

- Bundle and minify a JavaScript application:

`ncc build --minify {{path/to/file.js}}`

- Bundle and minify a JavaScript application with source maps:

`ncc build --source-map {{path/to/file.js}}`

- Automatically recompile on changes to application files:

`ncc build --watch {{path/to/file.js}}`

- Bundle into a temporary directory and run a JavaScript application for testing:

`ncc run {{path/to/file.js}}`

- Clean the `ncc` cache:

`ncc clean cache`
