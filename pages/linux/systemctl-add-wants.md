# systemctl add-wants

> Add `Wants` dependencies to a target for one or more units.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#add-wants%20TARGET%0A%20%20%20%20%20%20%20%20%20%20UNIT%E2%80%A6>.

- Add a `Wants` dependency from a target to a unit:

`systemctl add-wants {{target}} {{unit}}`

- Add multiple `Wants` dependencies at once:

`systemctl add-wants {{target}} {{unit1 unit2 ...}}`

- Add a user-level `Wants` dependency:

`systemctl add-wants {{target}} {{unit}} --user`
