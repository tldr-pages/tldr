# ykman fido

> 管理 YubiKey FIDO 应用程序。
> 更多信息：<https://docs.yubico.com/software/yubikey/tools/ykman/FIDO_Commands.html>。

- 显示关于 FIDO2 应用程序的一般信息：

`ykman fido info`

- 更改 FIDO PIN：

`ykman fido access change-pin`

- 列出存储在 YubiKey 上的常驻凭据：

`ykman fido credentials list`

- 从 YubiKey 中删除常驻凭据：

`ykman fido credentials delete {{id}}`

- 列出存储在 YubiKey 上的指纹（需要具有指纹传感器的密钥）：

`ykman fido fingerprints list`

- 向 YubiKey 添加新指纹：

`ykman fido fingerprints add {{name}}`

- 从 YubiKey 中删除指纹：

`ykman fido fingerprints delete {{name}}`

- 清除所有 FIDO 凭据（在超出 PIN 重试次数后必须执行此操作）：

`ykman fido reset`