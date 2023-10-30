# cargo logout

> Remove an API token from the registry locally.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-logout.html>.

- Remove the API token from the local credential storage:

`cargo logout`

- Specify the name of the registry to use (registry names can be defined in the config - the default is <https://crates.io>):

`cargo logout --registry {{name}}`
