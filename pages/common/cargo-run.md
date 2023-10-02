# cargo run

> To run the current package.
> Set the working directory of the binary executed to the current working directory.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-run.html>.

- Run the specified binary:

`cargo run --bin {{name}}`

- Run the specified example:

`cargo run --example {{name}}`

- Space or comma separated list of features to activate:

`cargo run --features {{features}}`

- Disable the default feature of the selected packages:

`cargo run --no-default-features`

- Activate all available features of selected packages:

`cargo run --all-features`

- Run with the given profile:

`cargo run --profile {{name}}`
