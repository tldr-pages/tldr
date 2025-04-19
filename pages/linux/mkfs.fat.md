# mkfs.fat

> Create an MS-DOS filesystem inside a partition.
> More information: <https://manned.org/mkfs.fat>.

- Create a fat filesystem inside partition `Y` on device `X`:

`mkfs.fat {{/dev/sdXY}}`

- Create filesystem with a volume-name:

`mkfs.fat -n {{volume_name}} {{/dev/sdXY}}`

- Create filesystem with a volume-id:

`mkfs.fat -i {{volume_id}} {{/dev/sdXY}}`

- Use 5 instead of 2 file allocation tables:

`mkfs.fat -f 5 {{/dev/sdXY}}`
