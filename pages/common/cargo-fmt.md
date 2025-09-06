# cargo fmt

> Run `rustfmt` on all source files in a Rust project.
> More information: <https://github.com/rust-lang/rustfmt>.

- Format all source files:

`cargo fmt`

- Check for formatting errors without writing to the files:

`cargo fmt --check`

- Pass arguments to each `rustfmt` call:

`cargo fmt -- {{rustfmt_args}}`
