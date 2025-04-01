# dolt fetch

> 从其他仓库下载对象和引用。
> 更多信息：<https://docs.dolthub.com/cli-reference/cli#dolt-fetch>.

- 从默认的远程上游仓库（origin）获取最新更改：

`dolt fetch`

- 从指定的远程上游仓库获取最新更改：

`dolt fetch {{remote_name}}`

- 使用远程仓库的当前状态更新分支，覆盖任何冲突的历史：

`dolt fetch -f`
