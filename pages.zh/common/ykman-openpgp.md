# ykman openpgp

> 管理 OpenPGP YubiKey 应用程序。
> 注意：对于某些设置，您需要使用 `gpg --card-edit`。
> 更多信息：<https://docs.yubico.com/software/yubikey/tools/ykman/OpenPGP_Commands.html>。

- 显示有关 OpenPGP 应用程序的一般信息：

`ykman openpgp info`

- 分别设置用户 PIN、重置代码和管理员 PIN 的重试次数：

`ykman openpgp access set-retries {{3}} {{3}} {{3}}`

- 更改用户 PIN、重置代码或管理员 PIN：

`ykman openpgp access change-{{pin|reset-code|admin-pin}}`

- 恢复 OpenPGP 应用程序的出厂设置（在超过管理员 PIN 重试次数后，您必须执行此操作）：

`ykman openpgp reset`