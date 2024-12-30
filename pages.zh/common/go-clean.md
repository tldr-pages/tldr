# go clean

> 删除对象文件和缓存文件。
> 更多信息：<https://golang.org/cmd/go/#hdr-Remove_object_files_and_cached_files>。

- 打印删除命令而不实际删除任何内容：

`go clean -n`

- 删除构建缓存：

`go clean -cache`

- 删除所有缓存的测试结果：

`go clean -testcache`

- 删除模块缓存：

`go clean -modcache`