# cargo rustdoc

> Generates package documentation.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-rustdoc.html>.

-  Build documentation of specified target:

`cargo rustdoc {{options}} --{{args}}`

- Open the docs in browser:

`cargo rustdoc --open`

- Specify package to document:

`cargo rustdoc --package {{spec}}`

- Document the package's library:

`cargo rustdoc --lib`

- Document specified binary:

`cargo rustdoc --bin {{name}}`

- Document specified example:

`cargo rustdoc --example {{name}}`

- Document integration test:

`cargo rustdoc --test {{name}}`

- Display help:

`cargo rustdoc --help`