# cargo run

> Run the current Cargo package.
> Note: the working directory of the executed binary will be set to the current working directory.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-run.html>.

- Run the default binary target:

`cargo run`

- Run the specified binary:

`cargo run --bin {{name}}`

- Run the specified example:

`cargo run --example {{name}}`

- Activate a space or comma separated list of features:

`cargo run --features {{feature1 feature2 ...}}`

- Disable the default features:

`cargo run --no-default-features`

- Activate all available features:

`cargo run --all-features`

- Run with the given profile:

`cargo run --profile {{name}}`
