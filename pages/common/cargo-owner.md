# cargo owner

> Manage the owners of a crate on the registry.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-owner.html>.

- Invite the given user or team as an owner:

`cargo owner --add {{username|github:org_name:team_name}} {{crate}}`

- Remove the given user or team as an owner:

`cargo owner --remove {{username|github:org_name:team_name}} {{crate}}`

- List owners of a crate:

`cargo owner --list {{crate}}`

- Specify the name of the registry to use (registry names can be defined in the configuration - <https://crates.io> by default):

`cargo owner --registry {{name}}`
