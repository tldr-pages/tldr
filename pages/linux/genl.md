# genl

> Query the generic netlink controller of the Linux kernel.
> More information: <https://manned.org/genl>.

- List all registered generic netlink families:

`genl ctrl list`

- Display information about a specific family by name:

`genl ctrl get name {{nlctrl|nl80211|...}}`

- Display information about a specific family by ID:

`genl ctrl get id {{family_id}}`

- Monitor generic netlink controller events:

`genl ctrl monitor`
