# cargo locate-project

> Print the full path to the `Cargo.toml` manifest of the current project.
> If the project is part of a workspace, the manifest of the project is shown, rather than the workspace output.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-locate-project.html>.

- Print the JSON object to stdout with full path to `Cargo.toml` manifest:

`cargo locate-project`

- Print the project path in the specified format:

`cargo locate-project --message-format {{plain|json}}`

- Print the `Cargo.toml` located at the given path:

`cargo locate-project --manifest-path {{path/to/Cargo.toml}}`

- Print the `Cargo.toml` located at the root of workspace as opposed to current workspace member:

`cargo locate-project --workspace`