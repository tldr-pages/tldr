# cargo generate-lockfile

> Generates the `Cargo.lock` file for the current package.
> If the lockfile already exists it will be rebuilt with latest version of every package.
> More information: <https://doc.rust-lang.org/stable/cargo/commands/cargo-generate-lockfile.html>.

- Generate a `Cargo.lock` file with the latest version of every package:

`cargo generate-lockfile`

- Specify a custom path for the `Cargo.toml` file (Note: By default the file is present in the current directory):

`cargo generate-lockfile --manifest-path {{path/to/file.toml}}`

- Assert that the `Cargo.lock` file is up-to-date:

`cargo generate-lockfile --locked`

- Prevent Cargo from attempting to access the network to determine if it out-of-date:

`cargo generate-lockfile --frozen`

- Prevent Cargo from accessing the network. (Note: If Cargo requires internet to proceed and network is not available, it will stop with an error):

`cargo generate-lockfile --offline`
