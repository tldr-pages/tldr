# systemctl list-dependencies

> Show a unit's dependency tree in systemd.
> See also: `systemctl list-units` to list loaded units.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#list-dependencies%20UNIT%E2%80%A6>.

- Show the dependency tree of a unit (defaults to `default.target` if omitted):

`systemctl list-dependencies {{unit}}`

- Include all dependency types (not only `Requires=` and `Wants=`):

`systemctl list-dependencies {{unit}} {{[-a|--all]}}`

- Limit the tree to a specific unit type:

`systemctl list-dependencies {{unit}} --type {{service|socket|target|mount|...}}`

- Reverse the direction to show units that depend on the specified unit:

`systemctl list-dependencies {{unit}} --reverse`

- Print output without headers or footers (for scripts):

`systemctl list-dependencies {{unit}} --no-legend`


