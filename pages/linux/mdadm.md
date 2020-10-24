# mdadm

> RAID management utility.
> More information: <https://linux.die.net/man/8/mdadm>.

- Create array:

`mdadm --create {{/dev/md/MyRAID}} --level {{raid_level}} --raid-devices {{number_of_disks}} {{/dev/sdXN}}`

- Stop array:

`mdadm --stop {{/dev/md0}}`

- Mark disk as failed:

`mdadm --fail {{/dev/md0}} {{/dev/sdXN}}`

- Remove disk:

`mdadm --remove {{/dev/md0}} {{/dev/sdXN}}`

- Add disk to array:

`mdadm --assemble {{/dev/md0}} {{/dev/sdXN}}`

- Show RAID info:

`mdadm --detail {{/dev/md0}}`
