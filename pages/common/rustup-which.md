# rustup which

> Display which binary will be run for a command managed by `rustup`.
> Like `which`, but searches a Rust toolchain instead of `$PATH`.
> More information: <https://rust-lang.github.io/rustup>.

- Display the path to the binary in the default toolchain:

`rustup which {{command}}`

- Display the path to the binary in the specified toolchain (see `rustup help toolchain` for more information):

`rustup which --toolchain {{toolchain}} {{command}}`
