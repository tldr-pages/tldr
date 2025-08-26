# vgcfgbackup

> Back up volume group configuration metadata to files (not user data).
> More information: <https://manned.org/vgcfgbackup>.

- Back up metadata for all volume groups (to `/etc/lvm/backup/` by default):

`vgcfgbackup`

- Back up metadata for a specific volume group:

`vgcfgbackup {{vg_name}}`

- Write the backup to a specific file:

`vgcfgbackup {{[-f|--file]}} {{path/to/backup}} {{vg_name}}`

- Back up multiple VGs using a filename template (`%s` becomes the VG name):

`vgcfgbackup {{[-f|--file]}} {{/tmp/vg-backup-%s}} {{vg1 vg2 ...}}`

- Increase verbosity (repeat `-v` for more detail):

`vgcfgbackup {{[-v|--verbose]}} {{vg_name}}`
