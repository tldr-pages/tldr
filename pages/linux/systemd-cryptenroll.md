# systemd-cryptenroll

> Interactively enroll or remove methods used to unlock LUKS2-encrypted devices. Uses a password to unlock the device unless otherwise specified.
> In order to allow a partition to be unlocked during system boot, update the `/etc/crypttab` file or the initramfs.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-cryptenroll.html>.

- Enroll a new password (similar to `cryptsetup luksAddKey`):

`systemd-cryptenroll --password {{path/to/luks2_block_device}}`

- Enroll a new recovery key (i.e. a randomly generated passphrase that can be used as a fallback):

`systemd-cryptenroll --recovery-key {{path/to/luks2_block_device}}`

- List available tokens, or enroll a new PKCS#11 token:

`systemd-cryptenroll --pkcs11-token-uri {{list|auto|pkcs11_token_uri}} {{path/to/luks2_block_device}}`

- List available FIDO2 devices, or enroll a new FIDO2 device (`auto` can be used as the device name when there is only one token plugged in):

`systemd-cryptenroll --fido2-device {{list|auto|path/to/fido2_hidraw_device}} {{path/to/luks2_block_device}}`

- Enroll a new FIDO2 device with user verification (biometrics):

`systemd-cryptenroll --fido2-device {{auto|path/to/fido2_hidraw_device}} --fido2-with-user-verification yes {{path/to/luks2_block_device}}`

- Unlock using a FIDO2 device, and enroll a new FIDO2 device:

`systemd-cryptenroll --unlock-fido2-device {{path/to/fido2_hidraw_unlock_device}} --fido2-device {{path/to/fido2_hidraw_enroll_device}} {{path/to/luks2_block_device}}`

- Enroll a TPM2 security chip (only secure-boot-policy PCR) and require an additional alphanumeric PIN:

`systemd-cryptenroll --tpm2-device {{auto|path/to/tpm2_block_device}} --tpm2-with-pin yes {{path/to/luks2_block_device}}`

- Remove all empty passwords/all passwords/all FIDO2 devices/all PKCS#11 tokens/all TPM2 security chips/all recovery keys/all methods:

`systemd-cryptenroll --wipe-slot {{empty|password|fido2|pkcs#11|tpm2|recovery|all}} {{path/to/luks2_block_device}}`
