# pio access

> Set the access level on published resources (packages) in the registry.
> More information: <https://docs.platformio.org/en/latest/core/userguide/access/index.html>.

- Grant access to a resource for a specific user:

`pio access grant {{guest|maintainer|admin}} {{username}} {{resource_urn}}`

- Remove access to a resource for a specific user:

`pio access revoke {{username}} {{resource_urn}}`

- Show all resources a user or team can access, along with the access level:

`pio access list {{username}}`

- Set a resource to be privately accessible:

`pio access private {{resource_urn}}`

- Set a resource to be publicly accessible:

`pio access public {{resource_urn}}`
