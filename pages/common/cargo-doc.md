# cargo doc

> Build the documentation of Rust packages.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-doc.html>.

- Build the documentation for the current project and all dependencies:

`cargo doc`

- Do not build documentation for dependencies:

`cargo doc --no-deps`

- Build and open the documentation in a browser:

`cargo doc --open`

- Build and view the documentation of a particular package:

`cargo doc --open --package {{package}}`
