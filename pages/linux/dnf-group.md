# dnf group

> Manage virtual collections of packages on Fedora-based systems.
> More information: <https://dnf.readthedocs.io/en/latest/command_ref.html#group-command>.

- List DNF groups, showing installed and uninstalled status in a table:

`dnf {{[grp|group]}} list`

- Show DNF group info, including repository and optional packages:

`dnf {{[grp|group]}} info {{group_name}}`

- Install DNF group:

`dnf {{[grp|group]}} install {{group_name}}`

- Remove DNF group:

`dnf {{[grp|group]}} remove {{group_name}}`

- Upgrade DNF group:

`dnf {{[grp|group]}} upgrade {{group_name}}`
