# git hash-object

> 计算内容的唯一哈希键，并可选择性地创建指定类型的对象。
> 更多信息：<https://git-scm.com/docs/git-hash-object>.

- 计算对象 ID 但不存储：

`git hash-object {{path/to/file}}`

- 计算对象 ID 并将其存储在 Git 数据库中：

`git hash-object -w {{path/to/file}}`

- 指定对象类型计算对象 ID：

`git hash-object -t {{blob|commit|tag|tree}} {{path/to/file}}`

- 从 `stdin` 计算对象 ID：

`cat {{path/to/file}} | git hash-object --stdin`
