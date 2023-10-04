# cargo remove

> Remove dependencies from a `Cargo.toml` manifest file.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-remove.html>.

- Remove one or more dependencies from the `Cargo.toml` manifest:

`cargo remove {{dependency_name}}`

- Remove a build dependency:

`cargo remove --build {{dependency_name}}`

- Remove a dependency to the given target platform:

`cargo remove --target {{target}} {dependency_name}}`

- Don't actually write to the manifest:

`cargo remove --dry-run {{dependency_name}}`

- Display verbose output:

`cargo remove --verbose {{dependency_name}}`

- Do not print Cargo log message:

`cargo remove --quiet {{dependency_name}}`

- Specify package to remove from:

`cargo remove --package {{specification}} {dependency_name}}`

- Display help:

`cargo remove --help`
