# rustup-init.sh

> Script to install `rustup` and the Rust toolchain.
> More information: <https://forge.rust-lang.org/infra/other-installation-methods.html#rustup>.

- Download and run `rustup-init` to install `rustup` and the default Rust toolchain:

`curl https://sh.rustup.rs -sSf | sh -s`

- Download and run `rustup-init` and pass arguments to it:

`curl https://sh.rustup.rs -sSf | sh -s -- {{arguments}}`

- Run `rustup-init` and specify additional components or targets to install:

`rustup-init.sh --target {{target}} --component {{component}}`

- Run `rustup-init` and specify the default toolchain to install:

`rustup-init.sh --default-toolchain {{toolchain}}`

- Run `rustup-init` and do not install any toolchain:

`rustup-init.sh --default-toolchain {{none}}`

- Run `rustup-init` and specify an installation profile:

`rustup-init.sh --profile {{minimal|default|complete}}`

- Run `rustup-init` without asking for confirmation:

`rustup-init.sh -y`
