# hg 更新

> 将工作目录更新到指定的变更集。
> 更多信息：<https://www.mercurial-scm.org/doc/hg.1.html#update>。

- 更新到当前分支的最新提交：

`hg update`

- 更新到指定的修订版本：

`hg update --rev {{修订版本}}`

- 更新并丢弃未提交的更改：

`hg update --clean`

- 更新到与指定日期匹配的最后一次提交：

`hg update --date {{dd-mm-yyyy}}`