# userdbctl

> Inspect users, groups and group memberships on the system.
> More information: <https://www.freedesktop.org/software/systemd/man/userdbctl.html>.

- List all known user records:

`userdbctl user`

- Show details of a specific user:

`userdbctl user {{username}}`

- List all known groups:

`userdbctl group`

- Show details of a specific group:

`userdbctl group {{groupname}}`

- List all services currently providing user/group definitions to the system:

`userdbctl services`
