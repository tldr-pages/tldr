# mu

> 从本地 Maildir 索引和搜索邮件。
> 更多信息：<https://man.cx/mu>.

- 初始化邮件数据库，可选指定 Maildir 目录和电子邮件地址：

`mu init --maildir={{path/to/directory}} --my-address={{name@example.com}}`

- 索引新邮件：

`mu index`

- 使用特定关键字（在邮件正文、主题、发件人等中）查找邮件：

`mu find {{keyword}}`

- 查找主题为 `jellyfish` 的发送给 Alice 的邮件，包含 `apples` 或 `oranges`：

`mu find to:{{alice}} subject:{{jellyfish}} {{apples}} OR {{oranges}}`

- 在发送邮件文件夹中查找未读且主题以 `soc` 开头的邮件（`*` 只能在搜索词尾使用）：

`mu find 'subject:{{soc}}*' flag:{{unread}} maildir:'/{{Sent Items}}'`

- 查找 Sam 于 2021 年发送的大小在 2 KiB 到 2 MiB 之间且附带图片的邮件：

`mu find 'mime:{{image/*}} size:{{2k..2m}} date:{{20210101..20211231}} from:{{sam}}'`

- 列出姓名或电子邮件地址中包含 `Bob` 的联系人：

`mu cfind {{Bob}}`
