# postconf

> Postfix 配置工具。
> 此命令默认显示 `main.cf` 配置参数的值，并警告可能的参数名称拼写错误。它还可以更改 `main.cf` 配置参数的值。
> 更多信息：<https://manned.org/postconf>。

- 指定 `main.cf` 配置文件的目录，而不是默认配置目录：

`postconf -c {{path/to/configuration_directory}}`

- 编辑 `main.cf` 配置文件并使用 "name=value" 对更新参数设置：

`postconf -e`

- 打印 `main.cf` 的默认参数设置，而不是实际设置：

`postconf -d`

- 仅显示指定类别的参数。类别可以是内置（builtin）、服务（service）、用户（user）或全部（all）：

`postconf -C {{class}}`

- 列出可用于 Postfix SMTP 服务器的 SASL 插件类型。插件类型通过指定 `cyrus` 或 `dovecot` 作为名称，在 `smtpd_sasl_type` 配置参数中选择：

`postconf -a`

- 列出所有支持的查找表类型的名称。查找表在配置文件中指定为 `type:name`，其中类型可以是 `btree`、`cdb`、`hash`、`mysql` 等：

`postconf -m`