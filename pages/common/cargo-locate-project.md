# cargo locate-project

> Prints the JSON object to stdout with full path to the `Cargo.toml` manifest.
> If the project is part of a workspace, the manifest of the project is shown, rather than the workspace output.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-locate-project.html>.

- Print the JSON object to stdout with full path to `Cargo.toml` manifest:

`cargo locatte-project`

- Print the project path only and not the JSON object:

`cargo locate-project --message-format plain`

- Print the project path with JSON object:

`cargo locate-project --message-format json`

- Print the `Cargo.toml` located at the given path:

`cargo locate-project --manifest-path {{path/to/file.toml}}`
