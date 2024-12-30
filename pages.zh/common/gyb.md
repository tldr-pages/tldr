# gyb

> 使用 Gmail 的 API 通过 HTTPS 本地备份 Gmail 消息。
> 更多信息：<https://github.com/GAM-team/got-your-back>。

- 估算您 Gmail 帐户中所有电子邮件的数量和大小：

`gyb --email {{email@gmail.com}} --action estimate`

- 将 Gmail 帐户备份到特定目录：

`gyb --email {{email@gmail.com}} --action backup --local-folder {{path/to/directory}}`

- 仅备份 Gmail 帐户中的重要邮件或加星邮件到默认本地文件夹：

`gyb --email {{email@gmail.com}} --search "{{is:important OR is:starred}}"`

- 从本地文件夹恢复到 Gmail 帐户：

`gyb --email {{email@gmail.com}} --action restore --local-folder {{path/to/directory}}`