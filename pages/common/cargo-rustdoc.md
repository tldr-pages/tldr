# cargo rustdoc

> Generates package documentation.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-rustdoc.html>.

- Build documentation of the specified target:

`cargo rustdoc {{options}} --{{args}}`

- Open the documentation in the browser:

`cargo rustdoc --open`

- Specify the package to document:

`cargo rustdoc --package {{spec}}`

- Document the package's library:

`cargo rustdoc --lib`

- Document the specified binary:

`cargo rustdoc --bin {{name}}`

- Document the specified example:

`cargo rustdoc --example {{name}}`

- Document the specified integration test:

`cargo rustdoc --test {{name}}`

- Display help:

`cargo rustdoc --help`
