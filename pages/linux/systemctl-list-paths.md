# systemctl list-paths

> List path units currently in memory, ordered by path.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#list-paths%20PATTERN%E2%80%A6>.

- Show all path units currently in memory:

`systemctl list-paths`

- List path units matching specific wildcard pattern ie, `shell-globbing`:

`systemctl list-paths {{pattern}}`

- List path units that match with multiple patterns:

`systemctl list-paths {{pattern_1 pattern_2 ...}}`

- Show all path units, including inactive ones:

`systemctl list-paths --all`

- Filter path units by state:

`systemctl list-paths --state {{state}}`

- Also show unit types in the output:

`systemctl list-paths --show-types`
