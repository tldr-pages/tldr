# cargo logout

> Remove an API token from the registry locally.
> The token is used to authenticate to a package registry. You can add it back using `cargo login`.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-logout.html>.

- Remove an API token from the local credential storage (located in `$CARGO_HOME/credentials.toml`):

`cargo logout`

- Specify the name of the registry to use (registry names can be defined in the config - the default is <https://crates.io>):

`cargo logout --registry {{name}}`
