# crane registry

> 此命令在一个自动选择的端口（:0）、$PORT 或 --address 上提供一个注册表实现。
> 该命令会阻塞，直到服务器接受推送和拉取，内容可以存储在内存和磁盘中。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_registry_serve.md>.

- 提供注册表实现：

`crane registry serve`

- 监听的地址：

`crane registry serve --address {{address_name}}`

- 用于存储 blob 的目录路径：

`crane registry serve --disk {{path/to/store_dir}}`

- 显示 `crane registry` 的帮助信息：

`crane registry {{[-h|--help]}}`

- 显示 `crane registry serve` 的帮助信息：

`crane registry serve {{[-h|--help]}}`