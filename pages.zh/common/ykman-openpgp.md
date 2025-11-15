# ykman openpgp

> 管理 OpenPGP YubiKey 应用程序。
> 注意：你需要使用 `gpg --card-edit` 来进行某些设置。
> 更多信息：<https://docs.yubico.com/software/yubikey/tools/ykman/OpenPGP_Commands.html>.

- 显示有关 OpenPGP 应用程序的一般信息：

`ykman openpgp info`

- 分别设置用户 PIN码、复位代码和管理 PIN码的重试次数：

`ykman openpgp access set-retries {{3}} {{3}} {{3}}`

- 更改用户 PIN码、复位代码或管理 PIN码：

`ykman openpgp access change-{{pin|reset-code|admin-pin}}`

- 将 OpenPGP 应用程序恢复出厂设置（在超过管理 PIN码 重试次数后需要这样做）：

`ykman openpgp reset`
