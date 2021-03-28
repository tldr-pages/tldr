# pio org

> Manage PlatformIO organizations and their owners.
> More information: <https://docs.platformio.org/en/latest/core/userguide/org/>.

- Create a new organization:

`pio org create {{orgname}}`

- Delete an organization:

`pio org destroy {{orgname}}`

- Add a user to an organization:

`pio org add {{orgname}} {{username}}`

- Remove a user from an organization:

`pio org remove {{orgname}} {{username}}`

- List all organizations and their owners, the user owns:

`pio org list`

- Update the name, email or display name of an organization:

`pio org update --orgname {{new_orgname}} --email {{new_email}} --displayname {{new_displayname}} {{orgname}}`
