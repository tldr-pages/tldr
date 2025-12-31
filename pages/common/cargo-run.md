# cargo run

> Run the current Cargo package.
> Note: The working directory of the executed binary will be set to the current working directory.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-run.html>.

- Run the default binary target:

`cargo {{[r|run]}}`

- Run the specified binary:

`cargo {{[r|run]}} --bin {{name}}`

- Run the specified example:

`cargo {{[r|run]}} --example {{name}}`

- Activate a space or comma separated list of features:

`cargo {{[r|run]}} {{[-F|--features]}} "{{feature1 feature2 ...}}"`

- Disable the default features:

`cargo {{[r|run]}} --no-default-features`

- Activate all available features:

`cargo {{[r|run]}} --all-features`

- Run with the given profile:

`cargo {{[r|run]}} --profile {{name}}`
