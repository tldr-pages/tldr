# cargo msrv

> Manage the Minimum Supported Rust Version (MSRV) of a project.
> More information: <https://gribnau.dev/cargo-msrv>.

- Display the MSRVs of dependencies (as specified in their `Cargo.toml`):

`cargo msrv list`

- Find the MSRV of the project by trying to compile it with various toolchains:

`cargo msrv find`

- Show the MSRV of the project as specified in `Cargo.toml`:

`cargo msrv show`

- Set the MSRV in `Cargo.toml` to a given Rust version:

`cargo msrv set {{version}}`

- Verify whether the MSRV is satisfiable by compiling the project using the specified version of Rust:

`cargo msrv verify`
