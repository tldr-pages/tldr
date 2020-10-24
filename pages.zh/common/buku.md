# buku

> 命令行版本的书签管理器.
> 详见: <https://github.com/jarun/Buku>.

- 根据关键词和标签查找书签:

`buku {{keyword}} --stag {{privacy}}`

- 添加书签，并且打上标签:

`buku --add {{https://example.com}} {{search engine}}, {{privacy}}`

- 删除一个书签:

`buku --delete {{bookmark_id}}`

- 打开编辑器，修改书签:

`buku --write {{bookmark_id}}`

- 将指定标签移除:

`buku --update {{bookmark_id}} --tag {{-}} {{search engine}}`
