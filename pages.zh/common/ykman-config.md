# ykman config

> 启用或禁用 YubiKey 应用程序。
> 注意：您可以使用 `ykman info` 查看当前已启用的应用程序。
> 更多信息：<https://docs.yubico.com/software/yubikey/tools/ykman/Base_Commands.html#ykman-config-options-command-args>.

- 通过 USB 或 NFC 启用某个应用程序（`--enable` 可以多次使用以指定更多应用程序）：

`ykman config {{usb|nfc}} {{[-e|--enable]}} {{otp|u2f|fido2|oath|piv|openpgp|hsmauth}}`

- 通过 USB 或 NFC 禁用某个应用程序（`--disable` 可以多次使用以指定更多应用程序）：

`ykman config {{usb|nfc}} {{[-d|--disable]}} {{otp|u2f|fido2|oath|piv|openpgp|hsmauth}}`

- 禁用 NFC 上的所有应用程序：

`ykman config nfc {{[-D|--disable-all]}}`
