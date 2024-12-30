# chgrp

> 更改文件和目录的组所有权。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/chgrp-invocation.html>。

- 更改文件/目录的拥有组：

`chgrp {{group}} {{path/to/file_or_directory}}`

- 递归更改目录及其内容的拥有组：

`chgrp -R {{group}} {{path/to/directory}}`

- 更改符号链接的拥有组：

`chgrp -h {{group}} {{path/to/symlink}}`

- 将文件/目录的拥有组更改为匹配参考文件：

`chgrp --reference {{path/to/reference_file}} {{path/to/file_or_directory}}`