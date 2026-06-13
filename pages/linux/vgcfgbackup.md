# vgcfgbackup

> Back up volume group configuration metadata to files (not user data).
> More information: <https://manned.org/vgcfgbackup>.

- Back up metadata for all volume groups (to `/etc/lvm/backup/` by default):

`sudo vgcfgbackup`

- Back up metadata for a specific volume group:

`sudo vgcfgbackup {{vg_name}}`

- Write the backup to a specific file:

`sudo vgcfgbackup {{[-f|--file]}} {{path/to/backup}} {{vg_name}}`

- Back up multiple VGs using a filename template (`%s` becomes the VG name):

`sudo vgcfgbackup {{[-f|--file]}} {{/tmp/vg-backup-%s}} {{vg1 vg2 ...}}`

- Increase verbosity (repeat `-v` for more detail):

`sudo vgcfgbackup {{[-v|--verbose]}} {{vg_name}}`
