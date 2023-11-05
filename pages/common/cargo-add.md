# cargo add

> Add dependencies to a Rust project's `Cargo.toml` manifest.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-add.html>.

- Add the latest version of a dependency to the current project:

`cargo add {{dependency}}`

- Add a specific version of a dependency:

`cargo add {{dependency}}@{{version}}`

- Add a dependency and enable one or more specific features:

`cargo add {{dependency}} --features {{feature_1}},{{feature_2}}`

- Add an optional dependency, which then gets exposed as a feature of the crate:

`cargo add {{dependency}} --optional`

- Add a local crate as a dependency:

`cargo add --path {{path/to/crate_directory}}`

- Add a development or build dependency:

`cargo add {{dependency}} --{{dev|build}}`

- Add a dependency with all default features disabled:

`cargo add {{dependency}} --no-default-features`
