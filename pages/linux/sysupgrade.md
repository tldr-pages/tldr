# sysupgrade

> Upgrade OpenWrt firmware images and manage configuration backups.
> More information: <https://openwrt.org/docs/techref/sysupgrade>.

- Test a firmware image without flashing:

`sysupgrade {{[-T|--test]}} {{path/to/sysupgrade_image.bin}}`

- Upgrade with a firmware image and preserve configuration files:

`sysupgrade {{path/to/sysupgrade_image.bin}}`

- Upgrade with a firmware image without preserving configuration files:

`sysupgrade -n {{path/to/sysupgrade_image.bin}}`

- Create a backup archive of files configured for preservation:

`sysupgrade {{[-b|--create-backup]}} {{path/to/backup.tar.gz}}`

- Restore a backup archive without flashing a firmware image:

`sysupgrade {{[-r|--restore-backup]}} {{path/to/backup.tar.gz}}`

- List files that would be included in a backup archive:

`sysupgrade {{[-l|--list-backup]}}`

- Upgrade with a firmware image and restore configuration from a specific archive:

`sysupgrade -f {{path/to/config.tar.gz}} {{path/to/sysupgrade_image.bin}}`
