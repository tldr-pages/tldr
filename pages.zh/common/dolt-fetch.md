# dolt fetch

> 从另一个仓库下载对象和引用。
> 更多信息：<https://docs.dolthub.com/cli-reference/cli#dolt-fetch>。

- 从默认的远程上游仓库（origin）获取最新的更改：

`dolt fetch`

- 从特定的远程上游仓库获取最新的更改：

`dolt fetch {{remote_name}}`

- 使用远程的当前状态更新分支，覆盖任何冲突的历史：

`dolt fetch -f`