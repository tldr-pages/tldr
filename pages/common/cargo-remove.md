# cargo remove

> Remove dependencies from a Cargo.toml manifest file.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-remove.html>.

- Remove one or more depndencies from the Cargo.toml manifest:

`cargo remove`

- Remove as a development dependency:

`cargo remove --dev`

- Remove as a build dependency:

`cargo remove --build`

- Remove as a dependency to the given target platform:

`cargo remove --target {{target}}`

- Don't actually write to the manifest:

`cargo remove --dry-run`

- Use verbrose output:

`cargo remove {{-v|--verbose}}`

- Do not print cargo log messages:

`cargo remove {{-q|--quiet}}`

- Control when colored output is used:

`cargo remove --color {{auto|always|never}}`

- Path to the Cargo.toml file:

`cargo remove --manifest-path {{path}}`

- To assert that the Cargo.lock is up-to-date or want to avoid network access:

`cargo remove --frozen`
`cargo remove --locked`

- Prevents Cargo from accessing the network for any reason:

`cargo remove --offline`

- Package to remove from:

`cargo remove {{-p|--package}}  {{spec...}}`

- To specify toolchain for remove:

`cargo remove +{{stable|nightly}}`

- To override a configuration value:

`cargo remove --config {{KEY=VALUE|PATH}}`

- To change the current working directory before executing any specified operations:

`cargo remove -c {{PATH}}`

- Print help information:

`cargo remove {{-h|--help}}`

- Unstable (nightly-only) flags to Cargo:

`cargo -z help`