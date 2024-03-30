# ykman config

> Enable or disable YubiKey applications.
> Note: you can use `ykman info` to see currently enabled applications.
> More information: <https://docs.yubico.com/software/yubikey/tools/ykman/Base_Commands.html#ykman-config-options-command-args>.

- Enable an application over USB or NFC (`--enable` can be used multiple times to specify more applications):

`ykman config {{usb|nfc}} --enable {{otp|u2f|fido2|oath|piv|openpgp|hsmauth}}`

- Disable an application over USB or NFC (`--disable` can be used multiple times to specify more applications):

`ykman config {{usb|nfc}} --disable {{otp|u2f|fido2|oath|piv|openpgp|hsmauth}}`

- Disable all applications over NFC:

`ykman config nfc --disable-all`
