# trunk

> A modern tool for bundling and serving Rust web apps with CI/CD pipelines.
> More information: <https://docs.trunk.io/references/cli>.

- Start local/production server with hot reloading:

`trunk serve {{--port ...}} {{--release}} {{--proxy-backend=...}}`

- Build for production at root or subdirectory:

`trunk build --release {{--dist path/to/dist}} {{--public-url /path/to/app/subdir}}`

- List all available tools in the repo and if they are enabled:

`trunk tools list`

- Enable/disable a tool at a specific version:

`trunk tools {{enable/disable}} <tool>[@version]`

- Print an action's execution history:

`trunk actions histoty <action>`
