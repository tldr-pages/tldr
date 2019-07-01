# rdpsign

> 用于签名远程桌面协议（RDP）文件的工具.

- 为一个RDP文件签名:

`rdpsign {{文件路径.rdp}}`

- 使用一个指定的sha256哈希值为RDP文件签名:

`rdpsign {{文件路径.rdp}} /sha265 {{哈希值}}`

- 启用静默输出:

`rdpsign {{文件路径.rdp}} /q`

- 显示详细的信息、警告和状态:

`rdpsign {{文件路径.rdp}} /v`

- 在不更新文件的情况下将输出显示到标准输出来测试签名:

`rdpsign {{文件路径.rdp}} /l`
