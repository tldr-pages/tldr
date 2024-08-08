# dysk

> Display filesystem information in a pretty table.
> More information: <https://dystroy.org/dysk>.

- Standard overview of your usual disks:

'dysk'

- Sort by free size:

'dysk --sort free'

- Filter to include only HDD disks:

'dysk --filter 'disk = HDD''

- Filter to exclude SSD disks:

'dysk --filter 'disk <> SSD''

- Filter for high utilization or low free space:

'dysk --filter 'use > 65% | free < 50G''
