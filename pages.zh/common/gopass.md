# gopass

> 标准的 Unix 团队密码管理器。用 Go 编写。
> 更多信息：<https://www.gopass.pw>。

- 初始化配置设置：

`gopass init`

- 创建一个新条目：

`gopass new`

- 显示所有存储：

`gopass mounts`

- 挂载一个共享 Git 存储：

`gopass mounts add {{store_name}} {{git_repo_url}}`

- 使用关键字进行交互式搜索：

`gopass show {{keyword}}`

- 使用关键字搜索：

`gopass find {{keyword}}`

- 同步所有挂载的存储：

`gopass sync`

- 显示特定的密码条目：

`gopass {{store_name|path/to/directory|email@email.com}}`