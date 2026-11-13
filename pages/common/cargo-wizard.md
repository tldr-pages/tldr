# cargo wizard

> Cargo subcommand that applies predefined profile templates (fast-compile, fast-runtime, min-size) to `Cargo.toml`.
> More information: <https://github.com/kobzol/cargo-wizard>.

- Start an interactive wizard to configure a Cargo profile:

`cargo wizard`

- Apply a predefined template (`fast-compile`, `fast-runtime`, or `min-size`) to a specific Cargo profile:

`cargo wizard apply {{fast-compile|fast-runtime|min-size}} {{dev|release}}`