# pass

> 存储和读取密码或其它敏感数据。
> 所有数据都使用 GPG 加密，并通过 Git 仓库进行管理。
> 更多信息：<https://www.passwordstore.org>.

- 使用一个或多个 GPG ID 初始化（或重新加密）存储：

`pass init {{gpg_id_1}} {{gpg_id_2}}`

- 保存新密码和附加信息（在新行上按 `<Ctrl d>` 完成）：

`pass insert --multiline {{path/to/data}}`

- 编辑一个条目：

`pass edit {{path/to/data}}`

- 将密码（数据文件的第一行）复制到剪贴板：

`pass -c {{path/to/data}}`

- 列出整个存储树：

`pass`

- 生成一个指定长度的新随机密码，并将其复制到剪贴板：

`pass generate -c {{path/to/data}} {{num}}`

- 初始化一个新的 Git 仓库（由 pass 执行的任何更改将自动提交）：

`pass git init`

- 代表密码存储运行 Git 命令：

`pass git {{command}}`
