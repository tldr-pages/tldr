# pvremove

> Remove LVM labels from physical volume(s).
> More information: <https://manned.org/pvremove>.

- Remove a LVM label from a physical volume:

`sudo pvremove {{/dev/sdXY}}`

- Display detailed output during the operation:

`sudo pvremove --verbose {{/dev/sdXY}}`

- Remove a LVM label without asking for confirmation:

`sudo pvremove --yes {{/dev/sdXY}}`

- Forcefully remove a LVM label:

`sudo pvremove --force {{/dev/sdXY}}`

- Display output in JSON format:

`sudo pvremove --reportformat json {{/dev/sdXY}}`
