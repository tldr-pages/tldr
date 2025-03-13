# bacon

> A background code checker for Rust.
> More information: <https://github.com/Canop/bacon>.

- Run `cargo check` whenever a change is detected in the current directory:

`bacon`

- Run `cargo run` whenever a change is detected in the current directory:

`bacon run`

- Run `cargo test` whenever a change is detected in the given directory:

`bacon test --path {{path/to/directory}}`

- Run against all targets whenever a change is detected in the current directory:

`bacon --job check-all`

- Initialize a `bacon.toml` configuration file in the current directory:

`bacon --init`
