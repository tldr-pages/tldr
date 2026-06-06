# sysupgrade

> Upgrade OpenWrt firmware while preserving configuration files.
> More information: <https://openwrt.org/docs/techref/sysupgrade>.

- Upgrade using a firmware image and preserve configuration files:

`sysupgrade {{path/to/firmware_image.bin}}`

- Upgrade using a firmware image without preserving configuration files:

`sysupgrade -n {{path/to/firmware_image.bin}}`

- Create a backup archive of the current configuration:

`sysupgrade -b {{path/to/backup.tar.gz}}`

- Restore configuration from a backup archive:

`sysupgrade -r {{path/to/backup.tar.gz}}`

- Test an upgrade without writing the firmware:

`sysupgrade -T {{path/to/firmware_image.bin}}`