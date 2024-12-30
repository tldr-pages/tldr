# debchange

> 维护 Debian 源包的 debian/changelog 文件。
> 更多信息：<https://manned.org/debchange.1>。

- 为非维护者上传添加一个新版本到 changelog：

`debchange --nmu`

- 为当前版本添加一个 changelog 条目：

`debchange --append`

- 添加一个 changelog 条目以关闭指定 ID 的错误：

`debchange --closes {{bug_id}}`