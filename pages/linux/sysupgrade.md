# sysupgrade

> Upgrade OpenWrt firmware from an image, or back up and restore configuration files.
> By default, configuration in the files listed for backup is kept. An image may be a local file or an `http`/`https` URL.
> More information: <https://openwrt.org/docs/guide-user/installation/generic.sysupgrade>.

- Upgrade firmware and keep the current configuration:

`sysupgrade {{path/to/firmware.bin}}`

- Upgrade firmware without keeping the configuration:

`sysupgrade -n {{path/to/firmware.bin}}`

- Verify an image and a configuration archive without flashing:

`sysupgrade {{[-T|--test]}} {{path/to/firmware.bin}}`

- Flash an image even if the image checks fail:

`sysupgrade {{[-F|--force]}} {{path/to/firmware.bin}}`

- Create a configuration backup and exit without flashing:

`sysupgrade {{[-b|--create-backup]}} {{path/to/backup.tar.gz}}`

- Restore a configuration backup and exit without flashing:

`sysupgrade {{[-r|--restore-backup]}} {{path/to/backup.tar.gz}}`

- List the files that a configuration backup would include:

`sysupgrade {{[-l|--list-backup]}}`
