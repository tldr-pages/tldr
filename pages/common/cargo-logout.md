# cargo logout

> Remove an API token from the registry locally.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-logout.html>.

- This command will remove the API token from the local credential storage:

`cargo logout`

- To add the name of the registry to use:

`cargo logout --registry {{registry}}`

- To use verbose output:

`cargo logout {{-v|--verbose}}`

- Do not print cargo log messages:

`cargo logout {{-q|--quit}}`

- Control when colored output is used:

`cargo logout --color {{auto|always|never}}`

- To specify which toolchain to use:

`cargo logout +{{stable|nightly}}`

- Override a Cargo configuration value:

`cargo logout --config {{KEY=VALUE|PATH}}`

- Change the current working directory before executing any specified operation:

`cargo logout -c {{PATH}}`

- Print help information:

`cargo logout {{-h|--help}}`

- Unstable (nightly-only) flag to Cargo:

`cargo -z help` 
