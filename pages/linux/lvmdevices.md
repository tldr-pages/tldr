# lvmdevices

> Manage the LVM devices file that lists block devices allowed for physical volumes.
> More information: <https://manned.org/lvmdevices>.

- List devices recorded in the devices file:

`sudo lvmdevices`

- Add a device to the devices file:

`sudo lvmdevices --adddev {{/dev/sdXN}}`

- Remove a device from the devices file:

`sudo lvmdevices --deldev {{/dev/sdXN}}`

- Add a physical volume by its PVID:

`sudo lvmdevices --addpvid {{PVID}}`

- Remove a physical volume by its PVID:

`sudo lvmdevices --delpvid {{PVID}}`

- Update the devices file after device names change:

`sudo lvmdevices --update`

- Check the devices file for problems:

`sudo lvmdevices --check`

- Display version:

`lvmdevices --version`
