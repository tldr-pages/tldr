# cargo remove

> Remove dependencies from a Rust project's `Cargo.toml` manifest.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-remove.html>.

- Remove a dependency from the current project:

`cargo remove {{dependency}}`

- Remove a development or build dependency:

`cargo remove --{{dev|build}} {{dependency}}`

- Remove a dependency of the given target platform:

`cargo remove --target {{target}} {{dependency}}`
