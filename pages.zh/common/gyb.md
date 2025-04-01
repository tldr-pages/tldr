# gyb

> 使用 Gmail 的 API 通过 HTTPS 本地备份 Gmail 消息。
> 更多信息：<https://github.com/GAM-team/got-your-back>.

- 估算 Gmail 账户上的所有邮件数量和大小：

`gyb --email {{email@gmail.com}} --action estimate`

- 将 Gmail 账户备份到指定目录：

`gyb --email {{email@gmail.com}} --action backup --local-folder {{path/to/directory}}`

- 仅备份 Gmail 账户中重要的或已加星的邮件到默认本地文件夹：

`gyb --email {{email@gmail.com}} --search "{{is:important OR is:starred}}"`

- 从本地文件夹恢复到 Gmail 账户：

`gyb --email {{email@gmail.com}} --action restore --local-folder {{path/to/directory}}`