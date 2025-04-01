# kwallet-query

> 读取和写入 KDE 钱包。
> 更多信息：<https://manned.org/kwallet-query>.

- 列出 `kdewallet` 中 `Passwords` 文件夹的所有条目：

`kwallet-query {{kdewallet}} {{[-l|--list-entries]}}`

- 列出指定文件夹中的所有条目：

`kwallet-query {{kdewallet}} {{[-l|--list-entries]}} {{[-f|--folder]}} {{folder_name}}`

- 列出所有可用的文件夹：

`kwallet-query  {{kdewallet}} {{[-l|--list-entries]}} {{[-f|--folder]}} ""`

- 显示帮助信息：

`kwallet-query {{[-h|--help]}}`