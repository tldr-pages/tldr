# cargo build

> Compile a local package and all of its dependencies.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-build.html>.

- Build the package or packages defined by the `Cargo.toml` manifest file in the local path:

`cargo build`

- Build artifacts in release mode, with optimizations:

`cargo build --release`

- Require that `Cargo.lock` is up to date:

`cargo build --locked`

- Build all packages in the workspace:

`cargo build --workspace`

- Build a specific package:

`cargo build --package {{package}}`

- Build only the specified binary:

`cargo --bin {{name}}`

- Build only the specified test target:

`cargo build --test {{testname}}`
