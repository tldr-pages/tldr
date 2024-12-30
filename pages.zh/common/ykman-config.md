# ykman 配置

> 启用或禁用 YubiKey 应用程序。
> 注意：您可以使用 `ykman info` 查看当前启用的应用程序。
> 更多信息：<https://docs.yubico.com/software/yubikey/tools/ykman/Base_Commands.html#ykman-config-options-command-args>。

- 通过 USB 或 NFC 启用应用程序（可以多次使用 `--enable` 来指定更多应用程序）：

`ykman config {{usb|nfc}} --enable {{otp|u2f|fido2|oath|piv|openpgp|hsmauth}}`

- 通过 USB 或 NFC 禁用应用程序（可以多次使用 `--disable` 来指定更多应用程序）：

`ykman config {{usb|nfc}} --disable {{otp|u2f|fido2|oath|piv|openpgp|hsmauth}}`

- 通过 NFC 禁用所有应用程序：

`ykman config nfc --disable-all`