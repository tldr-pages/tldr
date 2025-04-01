# git annex

> 使用 Git 管理文件，但不将其内容纳入版本控制。
> 当文件被附属时，其内容会被移动到一个键值存储中，并创建一个指向该内容的符号链接。
> 更多信息：<https://git-annex.branchable.com>。

- 使用 Git annex 初始化一个仓库：

`git annex init`

- 添加一个文件：

`git annex add {{path/to/file_or_directory}}`

- 显示文件或目录的当前状态：

`git annex status {{path/to/file_or_directory}}`

- 同步本地仓库与远程仓库：

`git annex sync {{remote}}`

- 获取文件或目录：

`git annex get {{path/to/file_or_directory}}`

- 显示帮助：

`git annex help`
