# fwupdmgr

> Update device firmware, including UEFI, using `fwupd`.
> `fwupdmgr` will complain about a read-only filesystem if /boot is not formatted in FAT32.
> See also: `fwupdtool`.
> More information: <https://github.com/fwupd/fwupd/blob/main/src/fwupdmgr.md>.

- Display all devices detected by `fwupd`:

`fwupdmgr get-devices`

- Download the latest firmware metadata from LVFS:

`fwupdmgr refresh`

- List the updates available for devices on your system:

`fwupdmgr get-updates`

- Install firmware updates:

`fwupdmgr update`
