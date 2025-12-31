# cryptsetup luksFormat

> Initialize a LUKS partition and the initial key slot (0) with a passphrase or keyfile.
> Note: This operation overwrites all data on the partition.
> More information: <https://manned.org/cryptsetup-luksFormat>.

- Initialize a LUKS volume with a passphrase:

`cryptsetup luksFormat {{/dev/sdXY}}`

- Initialize a LUKS volume with a keyfile:

`cryptsetup luksFormat {{/dev/sdXY}} {{path/to/keyfile}}`

- Initialize a LUKS volume with a passphrase and set its label:

`cryptsetup luksFormat --label {{label}} {{/dev/sdXY}}`
