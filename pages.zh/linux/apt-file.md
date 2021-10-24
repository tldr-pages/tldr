# apt-file

> 在 apt 软件包中查找文件，其中也包括未安装的软件。
> 更多信息：<https://manpages.debian.org/latest/apt-file/apt-file.1.html>.

- 更新元数据的数据库：

`sudo apt update`

- 查找包含指定文件或路径的软件包：

`apt-file {{search|find}} {{文件路径}}`

- 列出指定包的内容：

`apt-file {{show|list}} {{软件包名}}`

- 查找符合给定 `pattern` 中正则表达式的软件包：

`apt-file {{search|find}} --regexp {{正则表达式}}`
