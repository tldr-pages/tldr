# dysk

> Display filesystem information in a table.
> More information: <https://dystroy.org/dysk>.

- Get a standard overview of your usual disks:

`dysk`

- Sort by free size:

`dysk --sort free`

- Include only HDD disks:

`dysk --filter 'disk = HDD'`

- Exclude SSD disks:

`dysk --filter 'disk <> SSD'`

- Display disks with high utilization or low free space:

`dysk --filter 'use > 65% | free < 50G'`
