# dpigs

> 显示在 `apt` 系统中安装的包占用的最大空间。
> 更多信息：<https://manned.org/dpigs>。

- 显示系统中占用空间最大的 N 个包：

`dpigs --lines={{N}}`

- 使用指定的文件代替默认的 dpkg [s]tatus 文件：

`dpigs --status={{path/to/file}}`

- 显示系统中安装的二进制包的最大 [S]ource 包：

`dpigs --source`

- 以 [H]uman-readable 格式显示包大小：

`dpigs --human-readable`

- 显示帮助：

`dpigs --help`