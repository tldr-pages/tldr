# phpcpd

> 一个用于检测 PHP 代码中复制粘贴的工具。
> 更多信息：<https://github.com/sebastianbergmann/phpcpd>.

- 分析特定文件或目录中的重复代码：

`phpcpd {{path/to/file_or_directory}}`

- 使用模糊匹配变量名进行分析：

`phpcpd --fuzzy {{path/to/file_or_directory}}`

- 指定最少的相同行数（默认为 5 行）：

`phpcpd --min-lines {{number_of_lines}} {{path/to/file_or_directory}}`

- 指定最少的相同标记（默认为 70）：

`phpcpd --min-tokens {{number_of_tokens}} {{path/to/file_or_directory}}`

- 排除一个目录的分析（必须相对于源目录）：

`phpcpd --exclude {{path/to/excluded_directory}} {{path/to/file_or_directory}}`

- 将结果输出到 PHP-CPD XML 文件：

`phpcpd --log-pmd {{path/to/log_file}} {{path/to/file_or_directory}}`