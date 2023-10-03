# cargo remove

> Remove dependencies from a `Cargo.toml` manifest file.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-remove.html>.

- Remove one or more dependencies from the `Cargo.toml` manifest:

`cargo remove`

- Remove a build dependency:

`cargo remove --build`

- Remove a dependency to the given target platform:

`cargo remove --target {{target}}`

- Don't actually write to the manifest:

`cargo remove --dry-run`

- Display verbose output:

`cargo remove --verbose`

- Do not print Cargo log message:

`cargo remove --quiet`

- Specify package to remove from:

`cargo remove --package  {{specification}}`

- Display help:

`cargo remove --help`
