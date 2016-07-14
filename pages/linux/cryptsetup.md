# cryptsetup

> Manage plain dm-crypt and LUKS encrypted volumes.

- Initialize a LUKS volume (overwrites all data on the partition):

`cryptsetup luksFormat {{/dev/sda1}}`

- Open a LUKS volume and create a mapping at/dev/mapper/{{backup}}:

`cryptsetup luksOpen {{/dev/sda1}} {{backup}}`

- Remove an existing mapping:

`cryptsetup luksClose {{backup}}`
