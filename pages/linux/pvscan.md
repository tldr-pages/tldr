# pvscan

> List all physical volumes and manage their online status.
> More information: <https://manned.org/pvscan>.

- List all physical volumes:

`pvscan`

- Show the volume group that uses a specific physical volume:

`pvscan --cache --listvg {{/dev/sdX}}`

- Show logical volumes that use a specific physical volume:

`pvscan --cache --listlvs {{/dev/sdX}}`

- Display detailed information in JSON format:

`pvscan --reportformat json`
