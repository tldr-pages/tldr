# cargo binstall

> Install Rust binaries from CI artifacts.
> Falls back to `cargo install` (from source code) if there are no binaries available.
> More information: <https://github.com/cargo-bins/cargo-binstall>.

- Install a package from <https://crates.io>:

`cargo binstall {{package}}`

- Install a specific version of a package (latest by default):

`cargo binstall {{package}}@{{version}}`

- Install a package and disable confirmation prompts:

`cargo binstall {{[-y|--no-confirm]}} {{package}}`
