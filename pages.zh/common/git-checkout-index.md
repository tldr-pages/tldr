# git checkout-index

> 将文件从暂存区复制到工作区。
> 更多信息：<https://git-scm.com/docs/git-checkout-index>.

- 恢复自上次提交以来删除的所有文件：

`git checkout-index --all`

- 恢复自上次提交以来删除或修改的所有文件（强制覆盖）：

`git checkout-index --all --force`

- 恢复自上次提交以来修改的文件（忽略已删除的文件）：

`git checkout-index --all --force --no-create`

- 将最后一次提交的整个工作树导出到指定目录（注意结尾斜杠）：

`git checkout-index --all --force --prefix={{路径/到/导出目录/}}`
