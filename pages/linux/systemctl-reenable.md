# systemctl reenable

> Re-enable one or more units.
> Used when targets of a service change.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#reenable%20UNIT%E2%80%A6>.

- Re-enable a unit, restoring its default symlinks:

`systemctl reenable {{unit}}`

- Re-enable multiple units at once:

`systemctl reenable {{unit1 unit2 ...}}`

- Re-enable a unit and start it immediately:

`systemctl reenable {{unit}} --now`
