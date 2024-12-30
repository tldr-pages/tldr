# fwconsole

> 管理和配置您的 FreePBX 系统（PBX 服务器）。
> 更多信息：<https://sangomakb.atlassian.net/wiki/spaces/PG/pages/41779247/fwconsole+commands+13>。

- 重新加载 FreePBX 配置：

`fwconsole reload`

- 启动 Asterisk 以及 FreePBX 所需的其他命令：

`fwconsole start`

- 停止 Asterisk 以及 FreePBX 所需的其他命令：

`fwconsole stop`

- 查看和更新设置：

`fwconsole setting {{关键词}} {{新值}}`

- 列出可用的备份：

`fwconsole backup --list`

- 列出可用的 FreePBX 命令：

`fwconsole list`

- 更改 FreePBX 需要由 apache 用户拥有的所有文件和目录的所有权：

`fwconsole chown`