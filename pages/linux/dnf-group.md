# dnf group

> Manage collections of packages on Fedora-based systems.
> Note: DNF5 lists environments with `dnf environment`. `dnf group` no longer accepts the DNF4 aliases `grp` and `groups`.
> More information: <https://dnf5.readthedocs.io/en/latest/commands/group.8.html>.

- List groups:

`dnf group list`

- Show information about a group, including its packages:

`dnf group info {{group_name}}`

- Install a group:

`sudo dnf group install {{group_name}}`

- Remove a group:

`sudo dnf group remove {{group_name}}`

- Upgrade a group:

`sudo dnf group upgrade {{group_name}}`
