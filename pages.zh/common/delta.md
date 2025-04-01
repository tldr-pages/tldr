# delta

> 用于查看 Git 和 diff 输出的工具。
> 更多信息：<https://github.com/dandavison/delta>。

- 比较文件或目录：

`delta {{path/to/old_file_or_directory}} {{path/to/new_file_or_directory}}`

- 比较文件或目录，显示行号：

`delta --line-numbers {{path/to/old_file_or_directory}} {{path/to/new_file_or_directory}}`

- 比较文件或目录，以并排方式显示差异：

`delta --side-by-side {{path/to/old_file_or_directory}} {{path/to/new_file_or_directory}}`

- 比较文件或目录，忽略任何 Git 配置设置：

`delta --no-gitconfig {{path/to/old_file_or_directory}} {{path/to/new_file_or_directory}}`

- 比较文件或目录，根据终端模拟器的超链接规范渲染提交哈希、文件名和行号：

`delta --hyperlinks {{path/to/old_file_or_directory}} {{path/to/new_file_or_directory}}`

- 显示当前设置：

`delta --show-config`

- 显示支持的语言及其关联的文件扩展名：

`delta --list-languages`