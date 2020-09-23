# cargo rustc

> Compile a Rust package, and pass extra options to the compiler.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-rustc.html>.

- Build the package or packages defined by the `Cargo.toml` manifest file in the current working directory:

`cargo rustc`

- Build artifacts in release mode, with optimizations:

`cargo rustc --release`

- Compile with architecture-specific optimizations for the current CPU:

`cargo rustc --release -- -C target-cpu=native`

- Compile with speed optimization:

`cargo rustc -- -C opt-level {{1|2|3}}`

- Compile with [s]ize optimization (`z` also turns off loop vectorization):

`cargo rustc -- -C opt-level {{s|z}}`

- Check if your package uses unsafe code:

`cargo rustc --lib -- -D unsafe-code`

- Build a specific package:

`cargo rustc --package {{package}}`

- Build only the specified binary:

`cargo --bin {{name}}`
