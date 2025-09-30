# mkfs.fat

> Maak een MS-DOS bestandssysteem in een partitie.
> Meer informatie: <https://manned.org/mkfs.fat>.

- Maak een fat bestandssysteem binnen partitie `Y` op apparaat `X`:

`mkfs.fat {{/dev/sdXY}}`

- Maak een bestandssysteem met een volumenaam:

`mkfs.fat -n {{volume_naam}} {{/dev/sdXY}}`

- Maak een bestandssysteem met een volume-id:

`mkfs.fat -i {{volume_id}} {{/dev/sdXY}}`

- Gebruik 5 in plaats van 2 bestandstoewijzingstabellen:

`mkfs.fat -f 5 {{/dev/sdXY}}`

- Geef bestandssysteemtype op:

`mkfs.fat -F {{12|16|32}} {{/dev/sdXY}}`
