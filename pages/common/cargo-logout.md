# cargo logout

> Remove an API token from the registry locally.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-logout.html>.

- Remove the API token from the local credential storage:

`cargo logout`

- Add the name of the registry to use:

`cargo logout --registry {{registry}}`

- Display verbose output:

`cargo logout --verbose`

- Do not print Cargo log message:

`cargo logout --quiet`

- Control when colored output is used:

`cargo logout --color {{auto|always|never}}`

- Override a Cargo configuration value:

`cargo logout --config {{KEY=VALUE|PATH}}`

- Change the current directory before executing any specified operation:

`cargo logout -c {{PATH}}`

- Display help:

`cargo logout --help`
