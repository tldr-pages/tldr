# ykman oath

> 管理 OATH YubiKey 应用程序。
> `关键词` 可以是名称或发行者的一部分。
> 更多信息：<https://docs.yubico.com/software/yubikey/tools/ykman/OATH_Commands.html>.

- 显示有关 OATH 应用程序的一般信息：

`ykman oath info`

- 更改用于保护 OATH 账户的密码（添加 `--clear` 以移除密码）：

`ykman oath access change`

- 添加一个新账户（`--issuer` 是可选的）：

`ykman oath accounts add {{[-i|--issuer]}} {{发行者}} {{名称}}`

- 列出所有账户（及其发行者）：

`ykman oath accounts list`

- 列出所有账户及其当前的 TOTP/HOTP 代码（可通过关键词过滤列表）：

`ykman oath accounts code {{关键词}}`

- 重命名一个账户：

`ykman oath accounts rename {{关键词}} {{发行者:名称|名称}}`

- 删除一个账户：

`ykman oath accounts delete {{关键词}}`

- 删除所有账户并恢复出厂设置：

`ykman oath reset`
