# git bug

> 一个分布式缺陷跟踪工具，使用 Git 的内部存储，因此不会在您的项目中添加任何文件。
> 您可以将问题提交到与他人交互的同一个 Git 远程仓库，就像提交和分支一样。
> 更多信息：<https://github.com/MichaelMure/git-bug/blob/master/doc/md/git-bug.md>。

- 创建一个新的身份：

`git bug user create`

- 创建一个新的缺陷：

`git bug add`

- 将新的缺陷条目推送到远程仓库：

`git bug push`

- 拉取更新：

`git bug pull`

- 列出现有的缺陷：

`git bug ls`

- 使用查询过滤和排序缺陷：

`git bug ls "{{status}}:{{open}} {{sort}}:{{edit}}"`

- 通过文本内容搜索缺陷：

`git bug ls "{{search_query}}" baz`
