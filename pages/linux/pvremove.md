# pvremove

> Remove LVM labels from physical volume(s).
> More information: <https://man7.org/linux/man-pages/man8/pvremove.8.html>.

- Remove a LVM label from a physical volume:

`sudo pvremove {{/dev/sdXY}}`

- Display detailed output during the operation:

`sudo pvremove --verbose {{physical_volume}}`

- Remove LVM label without asking for confirmation:

`sudo pvremove --yes {{physical_volume}}`

- Forcefully remove LVM label:

`sudo pvremove --force {{physical_volume}}`

- Display output in JSON format:

`sudo pvremove --reportformat json {{physical_volume}}`
