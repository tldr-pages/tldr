# buku

> 命令行浏览器独立书签管理器。
> 更多信息：<https://github.com/jarun/Buku>。

- 显示所有匹配“关键词”和带有“隐私”标签的书签：

`buku {{关键词}} --stag {{隐私}}`

- 添加带有“搜索引擎”和“隐私”标签的书签：

`buku --add {{https://example.com}} {{搜索引擎}}, {{隐私}}`

- 删除一个书签：

`buku --delete {{书签_id}}`

- 打开编辑器编辑一个书签：

`buku --write {{书签_id}}`

- 从书签中移除“搜索引擎”标签：

`buku --update {{书签_id}} --tag {{-}} {{搜索引擎}}`