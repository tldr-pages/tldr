# sgdisk

> GUID partition table (GPT) manipulator for Linux and Unix.
> More information: <https://manned.org/sgdisk>.

- Display partition table:

`sgdisk -p {{/dev/device}}`

- Create a new GPT partition:

`sgdisk --new={{partition_number}}:{{start_sector}}:{{end_sector}} {{/dev/device}}`

- Delete a partition:

`sgdisk --delete={{partition_number}} {{/dev/device}}`

- Change partition type:

`sgdisk --typecode={{partition_number}}:{{type_code}} {{/dev/device}}`

- Set partition name:

`sgdisk --change-name={{partition_number}}:'{{partition_name}}' {{/dev/device}}`

- Create a hybrid MBR:

`sgdisk --hybrid 1:2:3 {{/dev/device}}`

- Convert MBR to GPT:

`sgdisk --mbrtogpt {{/dev/device}}`

- Wipe all data and partition table from disk:

`sgdisk --zap-all {{/dev/device}}`
