# git checkout-index

> 从索引中复制文件到工作树。
> 更多信息：<https://git-scm.com/docs/git-checkout-index>。

- 恢复自上次提交以来删除的任何文件：

`git checkout-index --all`

- 恢复自上次提交以来删除或更改的任何文件：

`git checkout-index --all --force`

- 恢复自上次提交以来更改的任何文件，忽略已被删除的文件：

`git checkout-index --all --force --no-create`

- 将最后一次提交时的整个目录树导出到指定目录（末尾的斜杠很重要）：

`git checkout-index --all --force --prefix={{path/to/export_directory/}}`
