# git stamp

> 在最后一次提交的信息中标记，可以引用来自你的缺陷跟踪系统的缺陷编号或链接到其评审页面。
> 属于 `git-extras` 的一部分。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-stamp>.

- 在最后一次提交的信息中标记，引用自你的缺陷跟踪系统的缺陷编号：

`git stamp {{issue_number}}`

- 在最后一次提交的信息中标记，链接到其评审页面：

`git stamp {{Review https://example.org/path/to/review}}`

- 在最后一次提交的信息中标记，用新的缺陷编号替换之前的所有缺陷编号：

`git stamp --replace {{issue_number}}`
