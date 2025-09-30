# rustup toolchain

> Manage Rust toolchains.
> See `rustup help toolchain` for more information about toolchains.
> More information: <https://rust-lang.github.io/rustup>.

- Install or update a given toolchain:

`rustup toolchain install {{toolchain}}`

- Uninstall a toolchain:

`rustup toolchain uninstall {{toolchain}}`

- List installed toolchains:

`rustup toolchain list`

- Create a custom toolchain by symlinking to a directory:

`rustup toolchain link {{custom_toolchain_name}} {{path/to/directory}}`
