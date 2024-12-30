# git stamp

> 给最后的提交消息加上标签，可以引用你的缺陷追踪器中的问题编号或链接到其审查页面。
> 是 `git-extras` 的一部分。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-stamp>。

- 给最后的提交消息加上标签，引用来自你的缺陷追踪器的问题编号：

`git stamp {{issue_number}}`

- 给最后的提交消息加上标签，链接到其审查页面：

`git stamp {{Review https://example.org/path/to/review}}`

- 给最后的提交消息加上标签，用新的问题替换之前的问题：

`git stamp --replace {{issue_number}}`