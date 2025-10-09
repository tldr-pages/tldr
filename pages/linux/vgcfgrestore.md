# vgcfgrestore

> Restore volume group configuration  (not user data).
> More information: <https://manned.org/vgcfgrestore>.
- vgcfgrestore restores the metadata of a VG from a text back up file produced by vgcfgbackup (to `/etc/lvm/backup/` by default):

`vgcfgrestore`

- Restore VG metadata from last backup.:

`vgcfgrestore {{vg_name}}`

- Restore VG metadata from specified backup-file :

`vgcfgrestore {{[-f|--file]}} {{path/to/backup-file}} {{vg_name}}`

- List all VG metadata backups:

`vgcfgrestore {{[-l|--list]}} {{vg_name}}`

- List one VG metadata backup file:

`vgcfgrestore {{[-l|--list -f|--fil]}} {{path/to/backup-file}} {{vg_name}}`

