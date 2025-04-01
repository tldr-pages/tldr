# debchange

> 维护 Debian 源包的 debian/changelog 文件。
> 更多信息：<https://manned.org/debchange.1>.

- 为非维护者上传添加新版本到更改日志：

`debchange --nmu`

- 向当前版本添加更改日志条目：

`debchange --append`

- 添加更改日志条目以关闭指定 ID 的错误：

`debchange --closes {{bug_id}}`