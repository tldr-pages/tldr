# devlink

> Manage devlink devices, typically network hardware such as NICs and switches.
> More information: <https://manned.org/devlink>.

- List all devlink devices:

`devlink dev show`

- Display information about a specific device, such as driver and firmware versions:

`devlink dev info {{pci/0000:01:00.0}}`

- List all devlink ports:

`devlink port show`

- Display the health reporters of all devices and their states:

`devlink health show`

- Display all devices in pretty-printed JSON format:

`devlink {{[-jp|--json --pretty]}} dev show`

- Monitor devlink events:

`devlink monitor`

- Reload the driver of a specific device:

`sudo devlink dev reload {{pci/0000:01:00.0}}`
