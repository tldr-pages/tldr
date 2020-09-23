# cargo clippy

> A collection of lints to catch common mistakes and improve your Rust code.
> More information: <https://github.com/rust-lang/rust-clippy>.

- Run checks over the code in the current directory:

`cargo clippy`

- Require that `Cargo.lock` is up to date:

`cargo clippy --locked`

- Run checks on all packages in the workspace:

`cargo clippy --workspace`

- Run checks for a package:

`cargo clippy --package {{package}}`

- Treat warnings as errors:

`RUSTFLAGS="-Dwarnings" cargo clippy -- -D warnings`

- Run checks and ignore warnings:

`cargo clippy -- -A warnings`

- Apply Clippy suggestion automatically (experimental and only supported on the nightly channel):

`cargo clippy --fix -Z unstable-options`
