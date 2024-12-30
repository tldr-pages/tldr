# kmutil

> 用于管理内核扩展（kexts）和磁盘上的 kext 集合的工具。
> 更多信息：<https://keith.github.io/xcode-man-pages/kmutil.8.html>。

- 查找操作系统上可用的 kext：

`kmutil find`

- 显示有关内核管理子系统的日志信息：

`kmutil log`

- 根据提供的选项检查和显示 kext 集合的内容：

`kmutil inspect {{options}}`

- 检查 kext 集合之间的一致性：

`kmutil check`

- 转储 kernelmanagerd 状态以进行调试：

`sudo kmutil dumpstate`

- 根据在结果中指定的路径加载一个或多个扩展：

`kmutil load --bundle-path {{path/to/extension.kext}}`