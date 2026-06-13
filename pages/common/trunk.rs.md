# trunk

> Bundle and serve Rust WASM web applications.
> More information: <https://trunkrs.dev/commands/>.

- Build the application in release mode and serve it locally:

`trunk serve --release`

- Build the application and serve it on a specific port:

`trunk serve {{[-p|--port]}} {{port}}`

- Build for production at a specific output directory:

`trunk build --release {{[-d|--dist]}} {{path/to/distribution}}`

- Build with a specific public URL path for hosting in a subdirectory:

`trunk build --release --public-url /{{path/to/app_subdirectory}}`

- Clean the output directory:

`trunk clean`
