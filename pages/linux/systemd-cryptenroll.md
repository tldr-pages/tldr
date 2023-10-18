# systemd-cryptenroll

> Interactively enroll or remove methods used to unlock LUKS2-encrypted partitions/block devices.
> In order to allow a partition to be unlocked during system boot using something other than a Password, also update the crypttab file and initramfs.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-cryptenroll.html>.

- Unlock using Password, and enroll a new/additional Password:

`systemd-cryptenroll --password {{path/to/luks2_block_device}}`

- Unlock using Password, and enroll a new/additional Recovery Key:

`systemd-cryptenroll --recovery-key {{path/to/luks2_block_device}}`

- Unlock using Password, and list available or enroll a new/additional PKCS#11 Token:

`systemd-cryptenroll --pkcs11-token-uri={{list|auto|pkcs11_token_uri}} {{path/to/luks2_block_device}}`

- Unlock using Password, and list available or enroll a new FIDO2-Device (using PIN and Presence/Touch if available):

`systemd-cryptenroll --fido2-device={{list|auto|path/to/fido2_hidraw_device}} {{path/to/luks2_block_device}}`

- Unlock using Password, and enroll a new FIDO2-Device with User Verification (Biometrics):

`systemd-cryptenroll --fido2-device={{auto|path/to/fido2_hidraw_device}} --fido2-with-user-verification=yes {{path/to/luks2_block_device}}`

- Unlock using a FIDO2-Device, and enroll a new FIDO2-Device:

`systemd-cryptenroll --unlock-fido2-device={{path/to/fido2_hidraw_unlock_device}} --fido2-device={{path/to/fido2_hidraw_enroll_device}} {{path/to/luks2_block_device}}`

- Unlock using Password, and enroll a TPM2 Security Chip (only secure-boot-policy PCR) and require additional alphanumeric PIN:

`systemd-cryptenroll --tpm2-device={{auto|path/to/tpm2_block_device}} --tpm2-with-pin=yes {{path/to/luks2_block_device}}`

- Unlock using Password, and remove all empty Passwords/all Passwords/all FIDO2-Devices/all PKCS#11 Tokens/all TMP2 Security Chips/all Recovery-Keys/all Methods:

`systemd-cryptenroll --wipe-slots={{empty|password|fido2|pkcs#11|tpm2|recovery|all}} {{path/to/luks2_block_device}}`
