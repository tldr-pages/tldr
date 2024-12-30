# git bug

> 一个分布式的错误跟踪器，使用 Git 的内部存储，因此不会在你的项目中添加任何文件。
> 你可以将问题提交到你用来与他人互动的同一个 Git 远程，类似于提交和分支。
> 更多信息：<https://github.com/MichaelMure/git-bug/blob/master/doc/md/git-bug.md>。

- 创建一个新的身份：

`git bug user create`

- 创建一个新的错误：

`git bug add`

- 将新的错误条目推送到远程：

`git bug push`

- 拉取更新：

`git bug pull`

- 列出现有的错误：

`git bug ls`

- 使用查询过滤和排序错误：

`git bug ls "{{status}}:{{open}} {{sort}}:{{edit}}"`

- 按文本内容搜索错误：

`git bug ls "{{search_query}}" baz`