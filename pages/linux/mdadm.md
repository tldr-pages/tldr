# mdadm

> RAID management utility

- create array

`mdadm --create {{/path/to/raid_device_file}} --level {{ raid level }} --raid-devices {{ number of disks}} {{/path/to/disk_device_file}}`

- stop array

`mdadm -S {{/path/to/raid_device_file}}`

- mark disk as failed

`mdadm {{/path/to/raid_device_file}} -f {{/path/to/disk_device_file}}`

- remove disk

`mdadm {{/path/to/raid_device_file}} -r {{/path/to/disk_device_file}}`

- add disk to array

`mdadm {{/path/to/raid_device_file}} -a {{/path/to/disk_device_file}}`

- show RAID info

`mdadm -D {{/path/to/raid_device_file}}`
