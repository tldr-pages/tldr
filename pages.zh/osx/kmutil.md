# kmutil

> 用于管理磁盘上的内核扩展（kexts）和内核扩展集合的工具。
> 更多信息：<https://keith.github.io/xcode-man-pages/kmutil.8.html>.

- 查找操作系统上的内核扩展：

`kmutil find`

- 显示内核管理子系统的日志信息：

`kmutil log`

- 根据提供的选项检查和显示内核扩展集合的内容：

`kmutil inspect {{options}}`

- 检查内核扩展集合之间的完整性：

`kmutil check`

- 用于调试的内核管理器状态转储：

`sudo kmutil dumpstate`

- 根据指定路径的结果加载一个或多个扩展：

`kmutil load --bundle-path {{path/to/extension.kext}}`
