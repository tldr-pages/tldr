# phpcbf

> 修复由 phpcs 检测到的违规行为。
> 更多信息：<https://github.com/squizlabs/PHP_CodeSniffer>。

- 修复指定目录中的问题（默认遵循 PEAR 标准）：

`phpcbf {{path/to/directory}}`

- 显示已安装编码标准的列表：

`phpcbf -i`

- 指定要验证的编码标准：

`phpcbf {{path/to/directory}} --standard {{standard}}`

- 指定逗号分隔的文件扩展名以在检查时包含：

`phpcbf {{path/to/directory}} --extensions {{file_extension1,file_extension2,...}}`

- 处理之前加载的文件的逗号分隔列表：

`phpcbf {{path/to/directory}} --bootstrap {{path/to/file1,path/to/file2,...}}`

- 不递归进入子目录：

`phpcbf {{path/to/directory}} -l`