# ncc

> Compile a Node.js application into a single file.
> Supports TypeScript, binary addons and dynamic requires.
> More information: <https://github.com/vercel/ncc#usage>.

- Bundle a Node.js application:

`ncc build {{path/to/file.js}}`

- Bundle and minify a Node.js application:

`ncc build {{[-m|--minify]}} {{path/to/file.js}}`

- Bundle and minify a Node.js application and generate source maps:

`ncc build {{[-s|--source-map]}} {{path/to/file.js}}`

- Automatically recompile on changes to source files:

`ncc build {{[-w|--watch]}} {{path/to/file.js}}`

- Bundle a Node.js application into a temporary directory and run it for testing:

`ncc run {{path/to/file.js}}`

- Clean the `ncc` cache:

`ncc clean cache`
