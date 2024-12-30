# mu

> 从本地 Maildir 索引和搜索电子邮件。
> 更多信息：<https://man.cx/mu>。

- 初始化电子邮件数据库， optionally 指定 Maildir 目录和电子邮件地址：

`mu init --maildir={{path/to/directory}} --my-address={{name@example.com}}`

- 索引新电子邮件：

`mu index`

- 使用特定关键字查找消息（在邮件正文、主题、发件人等中）：

`mu find {{keyword}}`

- 查找发给 Alice 的主题为 `jellyfish` 的消息，内容包含单词 `apples` 或 `oranges`：

`mu find to:{{alice}} subject:{{jellyfish}} {{apples}} OR {{oranges}}`

- 在发件箱中查找未读消息，主题以 `soc` 开头（`*` 仅在搜索词末尾有效）：

`mu find 'subject:{{soc}}*' flag:{{unread}} maildir:'/{{Sent Items}}'`

- 查找来自 Sam 的带有图像附件的消息，大小在 2 KiB 到 2 MiB 之间，撰写于 2021 年：

`mu find 'mime:{{image/*}} size:{{2k..2m}} date:{{20210101..20211231}} from:{{sam}}`

- 列出联系人中名称或电子邮件地址包含 `Bob` 的联系人：

`mu cfind {{Bob}}`