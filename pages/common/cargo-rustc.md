# cargo rustc

> Compile a Rust package. Similar to `cargo build`, but you can pass extra options to the compiler.
> See `rustc --help` for all available options.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-rustc.html>.

- Build the package and pass options to `rustc`:

`cargo rustc -- {{rustc_options}}`

- Build artifacts in release mode, with optimizations:

`cargo rustc --release`

- Compile with architecture-specific optimizations for the current CPU:

`cargo rustc --release -- -C target-cpu=native`

- Compile with speed optimizations:

`cargo rustc -- -C opt-level {{1|2|3}}`

- Compile with [s]ize optimizations (`z` also turns off loop vectorization):

`cargo rustc -- -C opt-level {{s|z}}`

- Check if your package uses unsafe code:

`cargo rustc --lib -- -D unsafe-code`

- Build a specific package:

`cargo rustc --package {{package}}`

- Build only the specified binary:

`cargo --bin {{name}}`
