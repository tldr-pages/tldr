# bacon

> A background code checker for Rust.
> More information: <https://github.com/Canop/bacon>.

- Run `cargo check` whenever a change is detected in the current directory:

`bacon`

- Run specific job whenever a change is detected in the current directory:

`bacon {{run|test|clippy|doc|...}}`

- Run `cargo test` whenever a change is detected in the given directory:

`bacon test {{path/to/directory}}`

- Run `cargo check` against all targets whenever a change is detected in the current directory:

`bacon check-all`

- Initialize a `bacon.toml` configuration file in the current directory:

`bacon --init`
