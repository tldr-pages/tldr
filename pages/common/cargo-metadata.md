# cargo metadata

> Output the workspace members and resolved dependencies of current package as JSON.
> Note: The output format is subject to change in future versions of Cargo.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-metadata.html>.

- Print the workspace members and resolved dependencies of the current package:

`cargo metadata`

- Print only the workspace members and do not fetch dependencies:

`cargo metadata --no-deps`

- Print metadata in a specific format based on the specified version:

`cargo metadata --format-version {{version}}`

- Print metadata with the `resolve` field including dependencies only for the given target triple (Note: the `packages` array will still include the dependencies for all targets):

`cargo metadata --filter-platform {{target_triple}}`
