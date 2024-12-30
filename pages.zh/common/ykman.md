# ykman

> YubiKey 管理器 - 配置 YubiKeys。
> 如果连接了多个 YubiKeys，您必须在子命令之前添加 `--device serial_number`。
> 更多信息：<https://docs.yubico.com/software/yubikey/tools/ykman/index.html>。

- 显示关于 YubiKey 的一般信息（序列号，固件版本，功能等）：

`ykman info`

- 列出连接的 YubiKeys，带有简短的一行描述（包括序列号）：

`ykman list`

- 查看启用和禁用应用程序的文档：

`tldr ykman config`

- 查看管理 FIDO 应用程序的文档：

`tldr ykman fido`

- 查看管理 OATH 应用程序的文档：

`tldr ykman oath`

- 查看管理 OpenPGP 应用程序的文档：

`tldr ykman openpgp`