# git replace

> 创建、列出和删除替换对象的引用。
> 更多信息：<https://git-scm.com/docs/git-replace>。

- 用不同的提交替换任何提交，保持其他提交不变：

`git replace {{object}} {{replacement}}`

- 删除给定对象的现有替换引用：

`git replace --delete {{object}}`

- 交互式编辑对象的内容：

`git replace --edit {{object}}`