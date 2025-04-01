# ldconfig

> 配置共享库依赖的符号链接和缓存。
> 更多信息：<https://manned.org/ldconfig>。

- 更新符号链接并重建缓存（通常在安装新库时运行）：

`sudo ldconfig`

- 更新指定目录的符号链接：

`sudo ldconfig -n {{path/to/directory}}`

- 打印缓存中的库，并检查指定的库是否存在：

`ldconfig -p | grep {{library_name}}`