# kwallet-query

> 读取和写入KDE钱包。
> 更多信息：<https://manned.org/kwallet-query>。

- 列出 `kdewallet` 的 `Passwords` 文件夹中的所有条目：

`kwallet-query {{kdewallet}} {{-l|--list-entries}}`

- 列出特定文件夹中的所有条目：

`kwallet-query {{kdewallet}} {{-l|--list-entries}} {{-f|--folder}} {{folder_name}}`

- 列出所有可用的文件夹：

`kwallet-query {{kdewallet}} {{-l|--list-entries}} {{-f|--folder}} ""`