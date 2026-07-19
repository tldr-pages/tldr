# sysupgrade

> Upgrade OpenWrt firmware and manage configuration backups from the command line.
> More information: <https://openwrt.org/docs/guide-user/installation/sysupgrade.cli>.

- Flash a firmware image and keep the current configuration:

`sysupgrade {{path/to/firmware.bin}}`

- Flash a firmware image without saving configuration:

`sysupgrade -n {{path/to/firmware.bin}}`

- Verify an image without flashing it:

`sysupgrade {{[-T|--test]}} {{path/to/firmware.bin}}`

- Force flashing even if image checks fail (dangerous):

`sysupgrade {{[-F|--force]}} {{path/to/firmware.bin}}`

- Create a configuration backup archive:

`sysupgrade {{[-b|--create-backup]}} {{path/to/backup.tar.gz}}`

- Restore a configuration backup archive:

`sysupgrade {{[-r|--restore-backup]}} {{path/to/backup.tar.gz}}`

- List files that would be included in a configuration backup:

`sysupgrade {{[-l|--list-backup]}}`

- Flash an image and restore configuration from a specific archive:

`sysupgrade -f {{path/to/backup.tar.gz}} {{path/to/firmware.bin}}`
