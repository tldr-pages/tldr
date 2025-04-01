# postconf

> Postfix 配置工具。
> 默认情况下，此命令显示 `main.cf` 配置参数的值，并警告可能拼写错误的参数名称。它还可以更改 `main.cf` 配置参数的值。
> 更多信息：<https://manned.org/postconf>。

- 指定 `main.cf` 配置文件的目录，而不是默认配置目录：

`postconf -c {{path/to/configuration_directory}}`

- 编辑 `main.cf` 配置文件并使用“name=value”对更新参数设置：

`postconf -e`

- 打印 `main.cf` 的默认参数设置，而不是实际设置：

`postconf -d`

- 仅显示指定类别的参数。类别可以是 builtin、service、user 或 all：

`postconf -C {{class}}`

- 列出 Postfix SMTP 服务器可用的 SASL 插件类型。插件类型可以通过指定 `cyrus` 或 `dovecot` 作为 `smtpd_sasl_type` 配置参数的名称来选择：

`postconf -a`

- 列出所有支持的查找表类型名称。查找表在配置文件中指定为 `type:name`，其中类型可以是 `btree`、`cdb`、`hash`、`mysql` 等：

`postconf -m`