# lvmsadc

> LVM system activity data collector (not supported under LVM2; prefer `dmstats`).
> More information: <https://manned.org/lvmsadc>.

- Run the collector (legacy LVM1 systems only):

`lvmsadc`

- Report I/O statistics using the device-mapper replacement:

`dmstats report {{/dev/mapper/device}}`
