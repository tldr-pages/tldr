# cryptsetup

> Manage plain dm-crypt and LUKS (Linux Unified Key Setup) encrypted volumes.

- Initialize a LUKS volume (overwrites all data on the partition):

`cryptsetup luksFormat {{/dev/sda1}}`

- Open a LUKS volume and create a decrypted mapping at /dev/mapper/{{target}}:

`cryptsetup luksOpen {{/dev/sda1}} {{target}}`

- Remove an existing mapping:

`cryptsetup luksClose {{target}}`

- Change the LUKS volume's passphrase:

`cryptsetup luksChangeKey {{/dev/sda1}}`
