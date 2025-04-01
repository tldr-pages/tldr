# curl

> 在 PowerShell 中，如果原版的 `curl` 程序（<https://curl.se>）未正确安装，此命令可能是 `Invoke-WebRequest` 的别名。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- 查看原版 `curl` 命令的文档：

`tldr curl -p common`

- 查看 PowerShell 的 `Invoke-WebRequest` 命令文档：

`tldr invoke-webrequest`

- 通过打印版本号检查 `curl` 是否正确安装。如果此命令返回错误，PowerShell 可能已将此命令替换为 `Invoke-WebRequest`：

`curl --version`
