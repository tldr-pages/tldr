# systemd-cgls

> Shows the contents of the selected Linux control group hierarchy in a tree.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-cgls.html>.

- Display the whole control group hierarchy on your system:

`systemd-cgls`

- To see a cgroup tree of a specific resource controller (e.g. `cpu` or `memory`), execute:

`systemd-cgls {{controller}}`

- Show the hierarchy of a specific systemd unit:

`systemd-cgls --unit {{unit}}`
