# gopass

> 适用于团队的标准化 Unix 密码管理器。使用 Go 语言编写。
> 更多信息：<https://www.gopass.pw>.

- 初始化配置设置：

`gopass init`

- 创建新条目：

`gopass new`

- 显示所有存储：

`gopass mounts`

- 挂载共享的 Git 存储：

`gopass mounts add {{store_name}} {{git_repo_url}}`

- 使用关键字进行交互式搜索：

`gopass show {{keyword}}`

- 使用关键字进行搜索：

`gopass find {{keyword}}`

- 同步所有已挂载的存储：

`gopass sync`

- 显示特定的密码条目：

`gopass {{store_name|path/to/directory|email@email.com}}`