# cryptsetup

> Manage plain dm-crypt and LUKS encrypted volumes.

- Format a drive (or a file) to make it a LUKS volume:

`cryptsetup luksFormat {{path/to/luks_volume_to_be}}`

- Open a volume so that you can access it decrypted on the fly at /dev/mapper/{{a}}:

`cryptsetup luksOpen {{path/to/luks_volume_to_be}} {{a}}`
