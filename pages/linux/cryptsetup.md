# cryptsetup

> Manage plain `dm-crypt` and LUKS (Linux Unified Key Setup) encrypted volumes.
> Some subcommands such as `luksFormat` have their own usage documentation.
> More information: <https://manned.org/cryptsetup>.

- Initialize a LUKS volume with a passphrase (overwrites all data on the partition):

`cryptsetup luksFormat {{/dev/sdXY}}`

- Open a LUKS volume and create a decrypted mapping at `/dev/mapper/mapping_name`:

`cryptsetup open {{/dev/sdXY}} {{mapping_name}}`

- Display information about a mapping:

`cryptsetup status {{mapping_name}}`

- Remove an existing mapping:

`cryptsetup close {{mapping_name}}`

- Change a LUKS volume's passphrase:

`cryptsetup luksChangeKey {{/dev/sdXY}}`
