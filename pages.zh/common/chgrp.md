# chgrp

> 更改文件和目录的所属组。
> 另请参阅：`chown`。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/chgrp-invocation.html>。

- 更改文件/目录的所属组：

`chgrp {{组名}} {{路径/到/文件或目录}}`

- 递归更改目录及其内容的所属组：

`chgrp {{[-R|--recursive]}} {{组名}} {{路径/到/目录}}`

- 更改符号链接的所属组：

`chgrp {{[-h|--no-dereference]}} {{组名}} {{路径/到/符号链接}}`

- 将文件/目录的所属组更改为与参考文件匹配：

`chgrp --reference {{路径/到/参考文件}} {{路径/到/文件或目录}}`
