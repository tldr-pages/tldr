# mkfs.fat

> Maak een MS-DOS bestandssysteem in een partitie.
> Meer informatie: <https://manned.org/mkfs.fat>.

- Maak een fat bestandssysteem binnen partitie `Y` op apparaat `X`:

`sudo mkfs.fat {{/dev/sdXY}}`

- Maak een bestandssysteem met een volumenaam:

`sudo mkfs.fat -n {{volume_naam}} {{/dev/sdXY}}`

- Maak een bestandssysteem met een volume-id:

`sudo mkfs.fat -i {{volume_id}} {{/dev/sdXY}}`

- Gebruik 4 in plaats van 2 bestandstoewijzingstabellen:

`sudo mkfs.fat -f 4 {{/dev/sdXY}}`

- Geef bestandssysteemtype op:

`sudo mkfs.fat -F {{12|16|32}} {{/dev/sdXY}}`
