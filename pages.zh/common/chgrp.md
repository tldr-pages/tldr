# chgrp

> 更改文件和目录的组所有权。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/chgrp-invocation.html>.

- 更改文件或目录的组所有权：

`chgrp {{group}} {{path/to/file_or_directory}}`

- 递归更改目录及其内容的组所有权：

`chgrp {{[-R|--recursive]}} {{group}} {{path/to/directory}}`

- 更改符号链接的组所有权：

`chgrp {{[-h|--no-dereference]}} {{group}} {{path/to/symlink}}`

- 将文件或目录的组所有权更改为与参考文件匹配：

`chgrp --reference {{path/to/reference_file}} {{path/to/file_or_directory}}`