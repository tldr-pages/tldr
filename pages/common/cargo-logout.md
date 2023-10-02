# cargo logout

> Remove an API token from the registry locally
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-logout.html>

- This command will remove the API token from the local credential storage.

`cargo logout`

- To add the name of the registry to use.

`cargo logout --registry **registry**`

- To use verbose output.

`cargo logout -v`
`cargo logout --verbose`

- Do not print cargo log messages.

`cargo logout -q`
`cargo logout --quiet`

- Control when colored output is used.

`cargo logout --color **when**`
`cargo logout --color auto`
`cargo logout --color always`
`cargo logout --color never`

- To specify which toolchain to use.

`cargo logout +**toolchain**`
`cargo logout +stable`
`cargo logout +nightly`

- Overrides a Cargo configuration value.

`cargo logout --config **KEY=VALUE** or **PATH**`

- Changes the current working directory before executing any specified operations.

`cargo logout -c **PATH**`

- Print help information.

`cargo logout -h`
`cargo logout --help`

- Unstable (nightly-only) flags to Cargo.

`cargo -z help`
 