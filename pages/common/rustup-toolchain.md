# rustup toolchain

> Manage Rust toolchains.
> More information: <https://rust-lang.github.io/rustup>.

- Install or update a given toolchain:

`rustup install {{toolchain}}`

- Uninstall a toolchain:

`rustup uninstall {{toolchain}}`

- List installed toolchains:

`rustup list`

- Create a custom toolchain by symlinking to a directory:

`rustup link {{custom_toolchain_name}} {{path/to/directory}}`

- Display help:

`rustup help toolchain`
