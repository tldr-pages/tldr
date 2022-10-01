# mdadm

> RAID management utility.
> More information: <https://manned.org/mdadm>.

- Create array:

`sudo mdadm --create {{/dev/md/MyRAID}} --level {{raid_level}} --raid-devices {{number_of_disks}} {{/dev/sdXN}}`

- Stop array:

`sudo mdadm --stop {{/dev/md0}}`

- Mark disk as failed:

`sudo mdadm --fail {{/dev/md0}} {{/dev/sdXN}}`

- Remove disk:

`sudo mdadm --remove {{/dev/md0}} {{/dev/sdXN}}`

- Add disk to array:

`sudo mdadm --assemble {{/dev/md0}} {{/dev/sdXN}}`

- Show RAID info:

`sudo mdadm --detail {{/dev/md0}}`

- Reset disk by deleting RAID metadata:

`sudo mdadm --zero-superblock {{/dev/sdXN}}`
