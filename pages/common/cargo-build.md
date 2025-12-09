# cargo build

> Compile a local package and all of its dependencies.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-build.html>.

- Build the package or packages defined by the `Cargo.toml` manifest file in the local path:

`cargo {{[b|build]}}`

- Build artifacts in release mode, with optimizations:

`cargo {{[b|build]}} {{[-r|--release]}}`

- Require that `Cargo.lock` is up to date:

`cargo {{[b|build]}} --locked`

- Build all packages in the workspace:

`cargo {{[b|build]}} --workspace`

- Build a specific package:

`cargo {{[b|build]}} {{[-p|--package]}} {{package}}`

- Build only the specified binary:

`cargo {{[b|build]}} --bin {{name}}`

- Build only the specified test target:

`cargo {{[b|build]}} --test {{test_name}}`
