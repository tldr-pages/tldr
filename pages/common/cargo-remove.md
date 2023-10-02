# cargo remove

> Remove dependencies from a Cargo.toml manifest file.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-remove.html>.

- Remove one or more dependency from the Cargo.toml manifest:

`cargo remove`

- Remove as a build dependency:

`cargo remove --build`

- Remove as a dependency to the given target platform:

`cargo remove --target {{target}}`

- Don't actually write to the manifest:

`cargo remove --dry-run`

- Use verbose output:

`cargo remove --verbose`

- Do not print cargo log message:

`cargo remove --quiet`

- Package to remove from:

`cargo remove {{-p|--package}}  {{spec...}}`

- Print help information:

`cargo remove --help`
