# git checkout-index

> 从索引复制文件到工作树。
> 更多信息：<https://git-scm.com/docs/git-checkout-index>。

- 恢复自上次提交以来删除的任何文件：

`git checkout-index --all`

- 恢复自上次提交以来删除或更改的任何文件：

`git checkout-index --all --force`

- 恢复自上次提交以来更改的任何文件，忽略任何已删除的文件：

`git checkout-index --all --force --no-create`

- 将上次提交时的整个树导出到指定目录（后面的斜杠很重要）：

`git checkout-index --all --force --prefix={{path/to/export_directory/}}`