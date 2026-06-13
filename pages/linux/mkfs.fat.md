# mkfs.fat

> Create an MS-DOS filesystem inside a partition.
> More information: <https://manned.org/mkfs.fat>.

- Create a fat filesystem inside partition `Y` on device `X`:

`sudo mkfs.fat {{/dev/sdXY}}`

- Create filesystem with a volume-name:

`sudo mkfs.fat -n {{volume_name}} {{/dev/sdXY}}`

- Create filesystem with a volume-id:

`sudo mkfs.fat -i {{volume_id}} {{/dev/sdXY}}`

- Use 4 instead of 2 file allocation tables:

`sudo mkfs.fat -f 4 {{/dev/sdXY}}`

- Specify filesystem type:

`sudo mkfs.fat -F {{12|16|32}} {{/dev/sdXY}}`
