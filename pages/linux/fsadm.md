# fsadm

> Check or resize a filesystem on a device.
> More information: <https://manned.org/fsadm>.

- Check a filesystem for errors:

`fsadm check {{/dev/vg_name/lv_name}}`

- Perform a dry-run resize to a specific size (no changes made):

`fsadm {{[-n|--dry-run]}} resize {{/dev/vg_name/lv_name}} {{10G}}`

- Grow a filesystem to fill the entire device (omit the size):

`fsadm resize {{/dev/vg_name/lv_name}}`

- Resize the filesystem and the underlying logical volume together:

`fsadm {{[-l|--lvresize]}} resize {{/dev/vg_name/lv_name}} {{100G}}`

- For ext2/3/4, unmount and resize offline:

`fsadm {{[-e|--ext-offline]}} resize {{/dev/vg_name/lv_name}} {{20G}}`
