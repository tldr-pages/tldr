# phpcbf

> 修复 phpcs 检测到的违规问题。
> 更多信息：<https://github.com/squizlabs/PHP_CodeSniffer>。

- 修复指定目录中的问题（默认使用 PEAR 标准）：

`phpcbf {{path/to/directory}}`

- 显示已安装的编码标准列表：

`phpcbf -i`

- 指定要验证的编码标准：

`phpcbf {{path/to/directory}} --standard {{standard}}`

- 指定用逗号分隔的文件扩展名，用于分析：

`phpcbf {{path/to/directory}} --extensions {{file_extension1,file_extension2,...}}`

- 用逗号分隔的在处理前需要加载的文件列表：

`phpcbf {{path/to/directory}} --bootstrap {{path/to/file1,path/to/file2,...)}}`

- 不递归进入子目录：

`phpcbf {{path/to/directory}} -l`
