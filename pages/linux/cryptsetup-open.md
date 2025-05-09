# cryptsetup open

> Create a decrypted mapping of an encrypted volume.
> Note: With TRIM enabled, minimal data leakage in form of freed block information, perhaps sufficient to determine the filesystem in use may occur.
> However, you still most likely want to enable it, because the data inside is still safe and SSDs without TRIM will wear out faster.
> More information: <https://manned.org/cryptsetup-open>.

- Open a LUKS volume and create a decrypted mapping at `/dev/mapper/mapping_name`:

`cryptsetup open {{/dev/sdXY}} {{mapping_name}}`

- Use a keyfile instead of a passphrase:

`cryptsetup open --key-file {{path/to/file}} {{/dev/sdXY}} {{mapping_name}}`

- Allow the use of TRIM on the device:

`cryptsetup open --allow-discards {{/dev/sdXY}} {{mapping_name}}`

- Write the `--allow-discards` option into the LUKS header (the option will then always be used when you open the device):

`cryptsetup open --allow-discards --persistent {{/dev/sdXY}} {{mapping_name}}`

- Open a LUKS volume and make the decrypted mapping read-only:

`cryptsetup open --readonly {{/dev/sdXY}} {{mapping_name}}`
