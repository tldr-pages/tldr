# pio access

> Set the access level on published resources (packages) in the registry.
> More information: <https://docs.platformio.org/en/latest/core/userguide/access/>.

- Grant a user access to a resource:

`pio access grant {{guest|maintainer|admin}} {{username}} {{resource_urn}}`

- Remove a user's access to a resource:

`pio access revoke {{username}} {{resource_urn}}`

- Show all resources that a user or team has access to and the access level:

`pio access list {{username}}`

- Restrict access to a resource to specific users or team members:

`pio access private {{resource_urn}}`

- Allow all users access to a resource:

`pio access public {{resource_urn}}`
