# buku

> 命令行版本的书签管理器。
> 更多信息：<https://github.com/jarun/Buku>.

- 根据关键词和标签查找书签：

`buku {{关键字}} --stag {{标签}}`

- 添加书签，并且打上标签：

`buku --add {{https://example.com}} {{搜索引擎}}, {{标签}}`

- 删除一个书签：

`buku --delete "{{书签 id}}"`

- 打开编辑器，修改书签：

`buku --write "{{书签 id}}"`

- 将指定标签移除：

`buku --update "{{书签 id}}" --tag {{-}} {{搜索引擎}}`
