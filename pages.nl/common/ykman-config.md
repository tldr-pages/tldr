# ykman config

> In- of uitschakelen van YubiKey applicaties.
> Opmerking: je kan `ykman info` gebruiken om de huidige ingeschakelde applicaties te zien.
> Meer informatie: <https://docs.yubico.com/software/yubikey/tools/ykman/Base_Commands.html#ykman-config-options-command-args>.

- Schakel een applicatie in via USB of NFC (`--enable` kan meerdere keren gebruikt worden om meerdere applicaties te specificeren):

`ykman config {{usb|nfc}} --enable {{otp|u2f|fido2|oath|piv|openpgp|hsmauth}}`

- Schakel een applicatie uit via USB of NFC (`--disable` kan meerdere keren gebruikt worden om meerdere applicaties te specificeren):

`ykman config {{usb|nfc}} --disable {{otp|u2f|fido2|oath|piv|openpgp|hsmauth}}`

- Schakel alle applicaties uit via NFC:

`ykman config nfc --disable-all`
