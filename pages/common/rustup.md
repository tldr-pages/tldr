# rustup

> Install, manage, and update Rust toolchains.
> Some subcommands, such as `toolchain`, `target`, `update`, etc. have their own usage documentation.
> More information: <https://rust-lang.github.io/rustup>.

- Install the nightly toolchain for your system:

`rustup install nightly`

- Switch the default toolchain to nightly so that the `cargo` and `rustc` commands will use it:

`rustup default nightly`

- Use the nightly toolchain when inside the current project but leave global settings unchanged:

`rustup override set nightly`

- Update all toolchains:

`rustup update`

- List installed toolchains:

`rustup show`

- Run `cargo build` with a certain toolchain:

`rustup run {{toolchain}} cargo build`

- Open the local Rust documentation in the default web browser:

`rustup doc`
