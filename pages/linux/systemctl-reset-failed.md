# systemctl reset-failed

> Reset the "failed" state of one or more units.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#reset-failed%20%5BPATTERN%E2%80%A6%5D>.

- Reset the failed state of all units:

`systemctl reset-failed`

- Reset the failed state of a specific unit:

`systemctl reset-failed {{unit}}`

- Reset multiple units at once:

`systemctl reset-failed {{unit_1 unit_2 ...}}`
