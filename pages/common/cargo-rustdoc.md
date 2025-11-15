# cargo rustdoc

> Build the documentation of Rust packages.
> Similar to `cargo doc`, but you can pass options to `rustdoc`. See `rustdoc --help` for all available options.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-rustdoc.html>.

- Pass options to `rustdoc`:

`cargo rustdoc -- {{rustdoc_options}}`

- Warn about a documentation lint:

`cargo rustdoc -- --warn rustdoc::{{lint_name}}`

- Ignore a documentation lint:

`cargo rustdoc -- --allow rustdoc::{{lint_name}}`

- Document the package's library:

`cargo rustdoc --lib`

- Document the specified binary:

`cargo rustdoc --bin {{name}}`

- Document the specified example:

`cargo rustdoc --example {{name}}`

- Document the specified integration test:

`cargo rustdoc --test {{name}}`
