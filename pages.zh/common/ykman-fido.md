# ykman fido

> 管理 YubiKey FIDO 应用程序。
> 更多信息：<https://docs.yubico.com/software/yubikey/tools/ykman/FIDO_Commands.html>.

- 显示 FIDO2 应用程序的一般信息：

`ykman fido info`

- 更改 FIDO 密码：

`ykman fido access change-pin`

- 列出存储在 YubiKey 上的常驻凭证：

`ykman fido credentials list`

- 从 YubiKey 中删除一个常驻凭证：

`ykman fido credentials delete {{ID}}`

- 列出存储在 YubiKey 上的指纹（需要带有指纹传感器的密钥）：

`ykman fido fingerprints list`

- 向 YubiKey 添加一个新指纹：

`ykman fido fingerprints add {{名称}}`

- 从 YubiKey 删除一个指纹：

`ykman fido fingerprints delete {{名称}}`

- 清除所有 FIDO 凭证（在超过密码重试次数之后需要执行此操作）：

`ykman fido reset`
