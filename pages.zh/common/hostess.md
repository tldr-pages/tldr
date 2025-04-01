# hostess

> 管理 `/etc/hosts` 文件。
> 更多信息：<https://github.com/cbednarski/hostess>.

- 列出域名、目标 IP 地址和启用/禁用状态：

`hostess list`

- 将指向本地机器的域名添加到 hosts 文件中：

`hostess add {{local.example.com}} {{127.0.0.1}}`

- 从 hosts 文件中移除一个域名：

`hostess del {{local.example.com}}`

- 禁用一个域名（但不移除）：

`hostess off {{local.example.com}}`