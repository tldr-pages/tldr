# cargo publish

> Upload a package to a registry.
> Note: You have to add an authentication token using `cargo login` before publishing a package.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-publish.html>.

- Perform checks, create a `.crate` file, and upload it to the registry:

`cargo publish`

- Simulate publishing, performing checks, and creating a `.crate` file without uploading it (equivalent of `cargo package`):

`cargo publish {{[-n|--dry-run]}}`

- Use the specified registry (registry names can be defined in the configuration - the default is <https://crates.io>):

`cargo publish --registry {{name}}`
