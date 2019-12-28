# cargo doc

> Build and view Rust package documentation offline.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-doc.html>.

- Build and view the default package documentation in the browser:

`cargo doc --open`

- Build documentation without accessing the network:

`cargo doc --offline`

- View a particular package's documentation:

`cargo doc --open --package {{package}}`

- View a particular package's documentation offline:

`cargo doc --open --offline --package {{package}}`
