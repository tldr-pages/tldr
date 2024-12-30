# rdpsign

> 一种用于签署远程桌面协议（RDP）文件的工具。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/rdpsign>。

- 签署一个 RDP 文件：

`rdpsign {{path\to\file.rdp}}`

- 使用特定的 sha256 哈希签署一个 RDP 文件：

`rdpsign {{path\to\file.rdp}} /sha265 {{hash}}`

- 启用静默输出：

`rdpsign {{path\to\file.rdp}} /q`

- 显示详细的警告、消息和状态：

`rdpsign {{path\to\file.rdp}} /v`

- 通过将输出显示到 `stdout` 来测试签署，而不更新文件：

`rdpsign {{path\to\file.rdp}} /l`