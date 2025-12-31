# dysk

> Display filesystem information in a table.
> More information: <https://manned.org/dysk>.

- Get a standard overview of your usual disks:

`dysk`

- Sort by free size:

`dysk {{[-s|--sort]}} free`

- Include only HDD disks:

`dysk {{[-f|--filter]}} 'disk = HDD'`

- Exclude SSD disks:

`dysk {{[-f|--filter]}} 'disk <> SSD'`

- Display disks with high utilization or low free space:

`dysk {{[-f|--filter]}} 'use > 65% | free < 50G'`
