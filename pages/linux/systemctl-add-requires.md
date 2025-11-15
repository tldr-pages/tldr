# systemctl add-requires

> Add `Requires` dependencies to a target for one or more units.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#add-wants%20TARGET%0A%20%20%20%20%20%20%20%20%20%20UNIT%E2%80%A6>.

- Add a `Requires` dependency from a target to a unit:

`systemctl add-requires {{target}} {{unit}}`

- Add multiple `Requires` dependencies at once:

`systemctl add-requires {{target}} {{unit1 unit2 ...}}`

- Add a user-level `Requires` dependency:

`systemctl add-requires {{target}} {{unit}} --user`
