# phpcpd

> 一个用于检测PHP代码中复制和粘贴的工具。
> 更多信息请访问：<https://github.com/sebastianbergmann/phpcpd>。

- 分析特定文件或目录中的重复代码：

`phpcpd {{path/to/file_or_directory}}`

- 使用模糊匹配分析变量名：

`phpcpd --fuzzy {{path/to/file_or_directory}}`

- 指定相同代码行的最小数量（默认为5）：

`phpcpd --min-lines {{number_of_lines}} {{path/to/file_or_directory}}`

- 指定相同标记的最小数量（默认为70）：

`phpcpd --min-tokens {{number_of_tokens}} {{path/to/file_or_directory}}`

- 从分析中排除一个目录（必须相对于源文件）：

`phpcpd --exclude {{path/to/excluded_directory}} {{path/to/file_or_directory}}`

- 将结果输出到PHP-CPD XML文件：

`phpcpd --log-pmd {{path/to/log_file}} {{path/to/file_or_directory}}`