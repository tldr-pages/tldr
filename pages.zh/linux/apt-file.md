# apt-file

> 在 `apt` 包中搜索文件，包括尚未安装的文件。
> 更多信息：<https://manned.org/apt-file.1>。

- 更新元数据数据库：

`sudo apt update`

- 搜索包含指定文件或路径的包：

`apt-file {{search|find}} {{partial_path/to/file}}`

- 列出特定包的内容：

`apt-file {{show|list}} {{package}}`

- 搜索与 `regular_expression` 匹配的包：

`apt-file {{search|find}} --regexp {{regular_expression}}`