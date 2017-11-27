# rustup

> Rust toolchain installer.
> Install, manage, and update Rust toolchains.

- Install the nightly toolchain for your system:

`rustup install nightly`

- Switch the default toolchain to nightly so that the cargo and rustc commands will use it:

`rustup default nightly`

- Update all toolchains:

`rustup update`

- List installed toolchains:

`rustup show`

- Run cargo build with a certain toolchain:

`rustup run {{toolchain name}} cargo build`