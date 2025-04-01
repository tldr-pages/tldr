# pro

> 管理 Ubuntu Pro 服务。
> 更多信息：<https://manned.org/ubuntu-advantage.1>.

- 将系统连接到 Ubuntu Pro 支持合约：

`sudo pro attach`

- 显示 Ubuntu Pro 服务的状态：

`pro status`

- 检查系统是否受到特定漏洞的影响（并在可能的情况下应用修复）：

`pro fix {{CVE-number}}`

- 显示不受支持的软件包数量：

`pro security-status`

- 列出已不再提供下载的软件包：

`pro security-status --unavailable`

- 列出第三方软件包：

`pro security-status --thirdparty`
