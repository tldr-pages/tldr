# cargo locate-project

> Print the full path to the `Cargo.toml` manifest of a project.
> If the project is part of a workspace, the manifest of the project is shown, rather than that of the workspace.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-locate-project.html>.

- Display the JSON object with full path to the `Cargo.toml` manifest:

`cargo locate-project`

- Display the project path in the specified format:

`cargo locate-project --message-format {{plain|json}}`

- Display the `Cargo.toml` manifest located at the root of the workspace as opposed to the current workspace member:

`cargo locate-project --workspace`

- Display the `Cargo.toml` manifest of a specific directory:

`cargo locate-project --manifest-path {{path/to/Cargo.toml}}`
