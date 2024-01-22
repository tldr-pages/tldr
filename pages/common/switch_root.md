# switch_root

> Use a different filesystem as the root of the mount tree.
> More information: <https://manned.org/switch_root.8>.

- Move `/proc`, `/dev`, `/sys` and `/run` to the specified filesystem, use this filesystem as the new root and start the specified init process:

`switch_root {{new_root}} {{init_process}}`

- Display help:

`switch_root -h`
