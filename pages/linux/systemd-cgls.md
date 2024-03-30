# systemd-cgls

> Show the contents of the selected Linux control group hierarchy in a tree.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-cgls.html>.

- Display the whole control group hierarchy on your system:

`systemd-cgls`

- Display a control group tree of a specific resource controller:

`systemd-cgls {{cpu|memory|io}}`

- Display the control group hierarchy of one or more systemd units:

`systemd-cgls --unit {{unit1 unit2 ...}}`
