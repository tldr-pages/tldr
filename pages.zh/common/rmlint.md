# rmlint

> 查找文件系统中的空间浪费和其他损坏。
> 更多信息：<https://rmlint.readthedocs.io/en/latest/rmlint.1.html>.

- 检查目录中的重复、空文件和损坏的文件：

`rmlint {{path/to/directory1 path/to/directory2 ...}}`

- 检查大于特定大小的重复文件，优先保留标记目录中的文件（在双斜杠后）：

`rmlint {{[-s|--size]}} {{1MB}} {{path/to/directory}} // {{path/to/original_directory}}`

- 检查空间浪费，保留未标记目录中的所有文件：

`rmlint {{[-k|--keep-all-untagged]}} {{path/to/directory}} // {{path/to/original_directory}}`

- 删除 `rmlint` 执行过程中找到的重复文件：

`./rmlint.sh`

- 基于数据查找重复的目录树，忽略名称：

`rmlint {{[-D|--merge-directories]}} {{path/to/directory}}`

- 标记路径较浅的文件为原始文件，如果深度相同则选择较短的文件：

`rmlint {{[-S|--rank-by]}} {{dl}} {{path/to/directory}}`

- 查找具有相同文件名和内容的文件，并链接而不是删除重复文件：

`rmlint {{[-c|--config]}} sh:link {{[-b|--match-basename]}} {{path/to/directory}}`

- 使用 `data` 作为主目录。只在 `backup` 中查找 `data` 中也存在的重复文件。不删除 `data` 中的任何文件：

`rmlint {{path/to/backup}} // {{path/to/data}} {{[-k|--keep-all-tagged]}} {{[-m|--must-match-tagged]}}`