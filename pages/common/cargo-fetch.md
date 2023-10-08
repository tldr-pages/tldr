# cargo fetch

> Fetch dependencies of a package from the network.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-fetch.html>.

- Fetch dependencies from the `Cargo.lock` file:

`cargo fetch {{options}}`

- Display verbose output:

`cargo fetch --verbose`

- Do not print Cargo log messages:

`cargo fetch --quiet`

- Control colored output:

`cargo fetch --color {{auto|always|never}}`

- Path to `Cargo.toml`:

`cargo fetch --manifest-path {{path}}`

- Prevent Cargo from accessing the network:

`cargo fetch --offline`

- Display help:

`cargo fetch --help`
