# iostat

> Report statistics for devices and partitions.

- Display a report of CPU and disk statistics since system startup:

`iostat`

- Display CPU statistics:

`iostat -c`

- Display disk statistics with disk names (including LVM):

`iostat -N`

- Display extended disk statistics with disk names for device "sda":

`iostat -xN {{sda}}`

- Display incremental reports of CPU and disk statistics every "interval" second(s) with units converted to megabytes:

`iostat -m {{interval}}`
