# ykman oath

> 管理 OATH YubiKey 应用程序。
> `keyword` 可以是名称或发行者的一部分。
> 更多信息：<https://docs.yubico.com/software/yubikey/tools/ykman/OATH_Commands.html>。

- 显示有关 OATH 应用程序的一般信息：

`ykman oath info`

- 更改用于保护 OATH 账户的密码（添加 `--clear` 以删除密码）：

`ykman oath access change`

- 添加新账户（`--issuer` 是可选的）：

`ykman oath accounts add --issuer {{issuer}} {{name}}`

- 列出所有账户（及其发行者）：

`ykman oath accounts list`

- 列出所有账户及其当前的 TOTP/HOTP 代码（可选地使用关键字过滤列表）：

`ykman oath accounts code {{keyword}}`

- 重命名账户：

`ykman oath accounts rename {{keyword}} {{issuer:name|name}}`

- 删除账户：

`ykman oath accounts delete {{keyword}}`

- 删除所有账户并恢复出厂设置：

`ykman oath reset`