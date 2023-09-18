# systemd-cryptenroll

> Interactively enroll or remove a Password, a FIDO2-Device / Security-Token, a TPM2 Security Chip, or a Recovery-Key used to unlock 
> a previously LUKS2-encrypted volume / block-device. The volume will need to be unlocked using a currently present Method. 
> In order to allow a volume to be unlocked during system boot using an enrolled PKCS#11-Token, TMP2 Security Chip or FIDO2-Device, 
> specify the respective option(s) in the crypttab File. systemd-cryptenroll does not change the allowed / possible unlock-Methods at system boot.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-cryptenroll.html>.

## Password

- Unlock using Password, and enroll a new / additional Password:

`systemd-cryptenroll --password {{path/to/luks2_block_device}}`

- Unlock using FIDO2-Device, and enroll a new / additional Password:

`systemd-cryptenroll --unlock-fido2-device={{auto|path/to/fido_hidraw_unlock_device}} --password {{path/to/luks2_block_device}}`

- Unlock using Key-File, and enroll a new / additional Password:

`systemd-cryptenroll --unlock-key-file={{path/to/key_file}} --password {{path/to/luks2_block_device}}`

- Unlock using Password, remove all currently present Passwords, and enroll a new Password:

`systemd-cryptenroll --wipe-slot=password --password {{path/to/luks2_block_device}}`

## Recovery-Key

- Unlock using Password, and enroll a new / additional Recovery-Key:

`systemd-cryptenroll --recovery-key {{path/to/luks2_block_device}}`

- Unlock using FIDO2-Device, and enroll a new / additional Recovery-Key:

`systemd-cryptenroll --unlock-fido2-device={{auto|path/to/fido_hidraw_unlock_device}} --recovery-key {{path/to/luks2_block_device}}`

- Unlock using Key-File, and enroll a new / additional Recovery-Key:

`systemd-cryptenroll --unlock-key-file={{path/to/key_file}} --recovery-key {{path/to/luks2_block_device}}`

- Unlock using Password, remove all currently present Recovery-Keys, and enroll a new Recovery-Key:

`systemd-cryptenroll --wipe-slot=recovery --recovery-key {{path/to/luks2_block_device}}`

## PKCS#11 Token

- List all connected / found PKCS#11 Token:

`systemd-cryptenroll --pkcs11-token-uri=list`

- Unlock using Password, and enroll a new / additional PKCS#11 Token:

`systemd-cryptenroll --pkcs11-token-uri={{auto|pkcs11_token_uri}} {{path/to/luks2_block_device}}`

- Unlock using FIDO2-Device, and enroll a new / additional PKCS#11 Token:

`systemd-cryptenroll --unlock-fido2-device={{auto|path/to/fido_hidraw_unlock_device}} --pkcs11-token-uri={{auto|pkcs11_token_uri}} {{path/to/luks2_block_device}}`

- Unlock using Key-File, and enroll a new / additional PKCS#11 Token:

`systemd-cryptenroll --unlock-key-file={{path/to/key_file}} --pkcs11-token-uri={{auto|pkcs11_token_uri}} {{path/to/luks2_block_device}}`

- Unlock using Password, remove all currently present PKCS#11 Token, and enroll a new PKCS#11 Token:

`systemd-cryptenroll --wipe-slot=pkcs11 --pkcs11-token-uri={{auto|pkcs11_token_uri}} {{path/to/luks2_block_device}}`

## FIDO2 Device

- List all connected FIDO2 Devices:

`systemd-cryptenroll --fido2-device=list`

- Unlock using Pasword, and enroll a new FIDO2-Device (using PIN and Presence/Touch if available):

`systemd-cryptenroll --fido2-device={{auto|path/to/fido_hidraw_device}} {{path/to/luks2_block_device}}`

- Unlock using Pasword, and enroll a new FIDO2-Device with User Vertification (Biometrics):

`systemd-cryptenroll --fido2-device={{auto|path/to/fido_hidraw_device}} --fido2-with-user-verification=yes {{path/to/luks2_block_device}}`

- Unlock using Pasword, remove all currently present FIDO2-Devices, and enroll a new FIDO2-Device:

`systemd-cryptenroll --wipe-slots=fido2 --fido2-device={{auto|path/to/fido_hidraw_device}} {{path/to/luks2_block_device}}`

- Unlock using a FIDO2-Device, and enroll a new FIDO2-Device:

`systemd-cryptenroll --unlock-fido2-device={{path/to/fido_hidraw_unlock_device}} --fido2-device={{path/to/fido_hidraw_enroll_device}} {{path/to/luks2_block_device}}` 

- Unlock using Key-File, and enroll a new FIDO2-Device:

`systemd-cryptenroll --unlock-key-file={{path/to/key_file}} --fido2-device={{auto|path/to/fido_hidraw_device}} {{path/to/luks2_block_device}}`

## TPM2 Security Chip

- List all available TPM2 Security Chips:

`systemd-cryptenroll --tpm2-device=list`

- Unlock using Password, and enroll a TPM2 Security Chip (only secure-boot-policy PCR):

`systemd-cryptenroll --tpm2-device={{auto|path/to/tpm_block_device}}`

- Unlock using a FIDO2-Device, and enroll a TPM2 Security Chip (only secure-boot-policy PCR):

`systemd-cryptenroll --unlock-fido2-device={{auto|path/to/fido_hidraw_unlock_device}} --tpm2-device={{auto|path/to/tpm_block_device}}`

- Unlock using a Key-File, and enroll a TPM2 Security Chip (only secure-boot-policy PCR):

`systemd-cryptenroll --unlock-key-file={{path/to/key_file}} --tpm2-device={{auto|path/to/tpm_block_device}}`

- Unlock using Password, and enroll a TPM2 Security Chip (only secure-boot-policy PCR) and require additional alphanumeric PIN:

`systemd-cryptenroll --tpm2-device={{auto|path/to/tpm_block_device}} --tpm2-with-pin=yes`

- Unlock using Password, and enroll a TPM2 Security Chip (self-selected PCRs):

`systemd-cryptenroll --tpm2-device={{auto|path/to/tpm_block_device}} --tpm2-pcrs={{list_of_selected_pcrs}}`

- Unlock using Password, and enroll a TPM2 Security Chip (self-defined PCR policy):

`systemd-cryptenroll --tpm2-device={{auto|path/to/tpm_block_device}} --tpm2-public-key={{path/to/pem_encoded_rsa_public_key_file}} --tpm2-public-key-pcrs={{list_of_selected_pcrs}} --tpm2-signature={{path/to/tpm2_pcr_signature_file}}`

## General

- Unlock using Password, and remove all empty Passwords / all Passwords / all FIDO2-Devices / all PKCS#11 Tokens / all TMP2 Security Chips / all Recovery-Keys:

`systemd-cryptenroll --wipe-slots={{empty|password|fido2|pkcs#11|tpm2|recovery}}`

- Unlock using Password, and remove all present Unlock Methods, and add a new one:

`systemd-cryptenroll --wipe-slots=all --{{password|fido2-device|pkcs11-token-uri|tpm2-device|recovery-key}} ...`
