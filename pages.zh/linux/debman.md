# debman

> 从未安装的包中读取手册页。
> 更多信息：<https://manned.org/debman.1>。

- 阅读由指定包提供的命令的手册页：

`debman -p {{package}} {{command}}`

- 指定要下载的包版本：

`debman -p {{package}}={{version}} {{command}}`

- 阅读 `.deb` 文件中的手册页：

`debman -f {{path/to/filename.deb}} {{command}}`