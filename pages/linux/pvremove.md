# pvremove

> Remove LVM labels from physical volume(s).
> More information: <https://manned.org/pvremove>.

- Remove an LVM label from a physical volume:

`sudo pvremove {{/dev/sdXY}}`

- Display detailed output during the operation:

`sudo pvremove {{[-v|--verbose]}} {{/dev/sdXY}}`

- Remove an LVM label without asking for confirmation:

`sudo pvremove {{[-y|--yes]}} {{/dev/sdXY}}`

- Forcefully remove an LVM label:

`sudo pvremove {{[-f|--force]}} {{/dev/sdXY}}`

- Display output in JSON format:

`sudo pvremove --reportformat json {{/dev/sdXY}}`
