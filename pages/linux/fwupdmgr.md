# fwupdmgr

> Update device firmware, including UEFI, using `fwupd`.
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

- Remount `/boot` with more privileges if update complains about a read-only filesystem:

`sudo mount {{[-o|--options]}} uid=1000,gid=1000,umask=0022 {{/dev/sdX}} /boot`

- Show firmware update history:

`fwupdmgr get-history`
