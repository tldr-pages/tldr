# lvmdevices

> Manage the LVM devices file that lists block devices allowed for physical volumes.
> More information: <https://manned.org/lvmdevices>.

- List devices recorded in the devices file:

`lvmdevices`

- Add a device to the devices file:

`lvmdevices --adddev {{/dev/sdXN}}`

- Remove a device from the devices file:

`lvmdevices --deldev {{/dev/sdXN}}`

- Add a physical volume by its PVID:

`lvmdevices --addpvid {{PVID}}`

- Remove a physical volume by its PVID:

`lvmdevices --delpvid {{PVID}}`

- Update the devices file after device names change:

`lvmdevices --update`

- Check the devices file for problems:

`lvmdevices --check`

- Display version:

`lvmdevices --version`
