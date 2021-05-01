# pio org

> Manage PlatformIO organizations and their owners.
> More information: <https://docs.platformio.org/en/latest/core/userguide/org/>.

- Create a new organization:

`pio org create {{organization_name}}`

- Delete an organization:

`pio org destroy {{organization_name}}`

- Add a user to an organization:

`pio org add {{organization_name}} {{username}}`

- Remove a user from an organization:

`pio org remove {{organization_name}} {{username}}`

- List all organizations the current user is a member of and their owners:

`pio org list`

- Update the name, email or display name of an organization:

`pio org update --orgname {{new_organization_name}} --email {{new_email}} --displayname {{new_display_name}} {{organization_name}}`
