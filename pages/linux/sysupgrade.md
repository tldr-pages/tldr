# sysupgrade

> Upgrade OpenWrt firmware images and manage configuration backups.
> More information: <https://openwrt.org/docs/techref/sysupgrade>.

- Upgrade to a new firmware image, preserving configuration:

`sysupgrade -v /{{path/to/firmware_image.bin}}`

- Upgrade to a new firmware image without preserving configuration:

`sysupgrade -n /{{path/to/firmware_image.bin}}`

- Verify a firmware image without flashing it:

`sysupgrade {{[-T|--test]}} /{{path/to/firmware_image.bin}}`

- Create a backup archive of files that would be preserved:

`sysupgrade {{[-b|--create-backup]}} /{{path/to/backup.tgz}}`

- Restore a backup archive without flashing a firmware image:

`sysupgrade {{[-r|--restore-backup]}} /{{path/to/backup.tgz}}`

- List files that would be preserved in a backup:

`sysupgrade {{[-l|--list-backup]}}`

- Display help:

`sysupgrade {{[-h|--help]}}`
