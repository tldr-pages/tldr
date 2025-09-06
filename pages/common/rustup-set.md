# rustup set

> Alter `rustup` settings.
> More information: <https://rust-lang.github.io/rustup>.

- Set the default host triple:

`rustup set default-host {{host_triple}}`

- Set the default profile (`minimal` includes only `rustc`, `rust-std` and `cargo`, whereas `default` adds `rust-docs`, `rustfmt` and `clippy`):

`rustup set profile {{minimal|default}}`

- Set whether `rustup` should update itself when running `rustup update`:

`rustup set auto-self-update {{enable|disable|check-only}}`
