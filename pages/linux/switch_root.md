# switch_root

> Use a different filesystem as the root of the mount tree.
> Note: switch_root will fail to function if the new root is not the root of a mount. Use bind-mounting as a workaround.
> See also: `chroot`, `mount`.
> More information: <https://manned.org/switch_root.8>.

- Move `/proc`, `/dev`, `/sys` and `/run` to the specified filesystem, use this filesystem as the new root and start the specified init process:

`switch_root {{new_root}} {{/sbin/init}}`

- Display help:

`switch_root -h`
