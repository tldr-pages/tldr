# buku

> 命令行版本的书签管理器。
> 更多信息：<https://github.com/jarun/Buku>.

- 根据关键词和标签“隐私”查找书签：

`buku {{关键词}} --stag {{隐私}}`

- 添加书签，并且打上标签“搜索引擎”和“隐私”：

`buku --add {{https://example.com}} {{搜索引擎}}, {{隐私}}`

- 删除一个书签：

`buku --delete {{书签 id}}`

- 打开编辑器，修改书签：

`buku --write {{书签 id}}`

- 移除一个书签中的标签“搜索引擎”：

`buku --update {{书签 id}} --tag {{-}} {{搜索引擎}}`
