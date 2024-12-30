# hostess

> 管理 `/etc/hosts` 文件。
> 更多信息：<https://github.com/cbednarski/hostess>。

- 列出域名、目标 IP 地址及其开/关状态：

`hostess list`

- 向你的 hosts 文件添加一个指向你机器的域名：

`hostess add {{local.example.com}} {{127.0.0.1}}`

- 从你的 hosts 文件中删除一个域名：

`hostess del {{local.example.com}}`

- 禁用一个域名（但不删除它）：

`hostess off {{local.example.com}}`