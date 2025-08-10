# systemd-cryptsetup

> Create or remove decrypted mappings of encrypted volumes. Equivalent of `cryptsetup open` and `cryptsetup close`.
> Arguments to this command are written exactly like a line in `/etc/crypttab`. It's used by systemd to unlock devices on boot.
> See also: `cryptsetup`.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-cryptsetup.html>.

- Open a LUKS volume and create a decrypted mapping at `/dev/mapper/mapping_name`:

`systemd-cryptsetup attach {{mapping_name}} {{/dev/sdXY}}`

- Open a LUKS volume with additional options and create a decrypted mapping at `/dev/mapper/mapping_name`:

`systemd-cryptsetup attach {{mapping_name}} {{/dev/sdXY}} none {{crypttab_options}}`

- Open a LUKS volume with a keyfile and create a decrypted mapping at `/dev/mapper/mapping_name`:

`systemd-cryptsetup attach {{mapping_name}} {{/dev/sdXY}} {{path/to/keyfile}} {{crypttab_options}}`

- Remove an existing mapping:

`systemd-cryptsetup detach {{mapping_name}}`
