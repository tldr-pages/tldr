# cargo publish

> Upload a package to a registry.
> Note: you have to add an authentication token using `cargo login` before publishing a package.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-publish.html>.

- Perform checks, create a `.crate` file and upload it to the registry:

`cargo publish`

- Perform checks, create a `.crate` file but don't upload it (equivalent of `cargo package`):

`cargo publish --dry-run`

- Specify the name of the registry to use (registry names can be defined in the config - the default is <https://crates.io>):

`cargo publish --registry {{name}}`
