# bcachefs device

> Manage devices within a running `bcachefs` filesystem.
> More information: <https://bcachefs-docs.readthedocs.io/en/latest/mgmt-devicemanagement.html>.

- Format and add a new device to an existing filesystem.:

`sudo bcachefs device add --label={{group}}.{{name}} {{path/to/mountpoint}} {{path/to/device}}`

- Migrate data off a device to prepare for removal:

`bcachefs device evacuate {{path/to/device}}`

- Permanently remove a device from a filesystem:

`bcachefs device remove {{path/to/device}}`
