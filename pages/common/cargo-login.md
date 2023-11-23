# cargo login

> Save an API token from the registry locally.
> The token is used to authenticate to a package registry. You can remove it using `cargo logout`.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-login.html>.

- Add an API token to the local credential storage (located in `$CARGO_HOME/credentials.toml`):

`cargo login`

- Specify the name of the registry to use (registry names can be defined in the config - the default is <https://crates.io>):

`cargo login --registry {{name}}`
