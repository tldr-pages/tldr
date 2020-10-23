# mdadm

> RAID management utility.
> More information: <https://linux.die.net/man/8/mdadm>.

- Create array:

`mdadm --create {{path/to/raid_device_file}} --level {{raid_level}} --raid-devices {{number_of_disks}} {{path/to/disk_device_file}}`

- Stop array:

`mdadm -S {{path/to/raid_device_file}}`

- Mark disk as failed:

`mdadm {{/dev/md0}} -f {{/dev/sdXN}}`

- Remove disk:

`mdadm {{path/to/raid_device_file}} -r {{path/to/disk_device_file}}`

- Add disk to array:

`mdadm {{path/to/raid_device_file}} -a {{path/to/disk_device_file}}`

- Show RAID info:

`mdadm -D {{path/to/raid_device_file}}`
