# cargo owner

> Manage the owners of a crate on the registry.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-owner.html>.

- Invite the given user or team as an owner:

`cargo owner {{[-a|--add]}} {{username|github:org_name:team_name}} {{crate}}`

- Remove the given user or team as an owner:

`cargo owner {{[-r|--remove]}} {{username|github:org_name:team_name}} {{crate}}`

- List owners of a crate:

`cargo owner {{[-l|--list]}} {{crate}}`

- Use the specified registry (registry names can be defined in the configuration - the default is <https://crates.io>):

`cargo owner --registry {{name}}`
