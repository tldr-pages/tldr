# systemctl list-dependencies

> Show a unit's dependency tree in systemd.
> See also: `systemctl list-units` to list loaded units.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#%0A%20%20%20%20%20%20%20%20%20%20%20%20list-dependencies%0A%20%20%20%20%20%20%20%20%20%20%20%20UNIT...%0A%20%20%20%20%20%20%20%20%20%20>.

- Show the dependency tree of `default.target`:

`systemctl list-dependencies`

- Show the dependency tree of a specific unit:

`systemctl list-dependencies {{unit}}`

- Include all dependency types (not only `Requires=` and `Wants=`):

`systemctl list-dependencies {{unit}} {{[-a|--all]}}`

- Limit the tree to a specific unit type:

`systemctl list-dependencies {{unit}} {{[-t|--type]}} {{service|socket|target|mount|...}}`

- Reverse the direction to show units that depend on the specified unit:

`systemctl list-dependencies {{unit}} --reverse`

- Print output without headers or footers (for scripts):

`systemctl list-dependencies {{unit}} --no-legend`
