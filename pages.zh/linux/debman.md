# debman

> 从未安装的软件包中读取手册页。
> 更多信息：<https://manned.org/debman.1>.

- 读取指定软件包中提供的命令的手册页：

`debman -p {{package}} {{command}}`

- 指定要下载的软件包版本：

`debman -p {{package}}={{version}} {{command}}`

- 读取 `.deb` 文件中的手册页：

`debman -f {{path/to/filename.deb}} {{command}}`