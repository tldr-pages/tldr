# systemctl reenable

> Reenable one or more units.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#reenable%20UNIT%E2%80%A6>

- Reenable a unit, restoring its default symlinks:

`systemctl reenable {{unit}}`

- Reenable multiple units at once:

`systemctl reenable {{unit1 unit2 ...}}`

- Reenable a unit and start it immediately:

`systemctl reenable {{unit}} --now`
