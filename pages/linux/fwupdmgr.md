# fwupdmgr

> A simple daemon that allows updating some device firmwares, including UEFI.
> More information: <https://fwupd.org/>.

- Display all devices detected by fwupd:

`fwupdmgr get-devices`

- Download the latest firmware metadata from LVFS:

`fwupdmgr refresh`

- List the updates available for devices on your system:

`fwupdmgr get-updates`

- Install firmware updates:

`fwupdmgr update`
